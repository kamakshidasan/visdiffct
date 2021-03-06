#### import the simple module from the paraview
from paraview.simple import *
import os, csv, sys
import subprocess
from helper import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

file_path = 'adhitya'
file_name = get_file_name(file_path)
parent_path = get_parent_path(file_path)

# create a new 'Legacy VTK Reader'
vtkFile = LegacyVTKReader(FileNames=[file_path])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
vtkFileDisplay = Show(vtkFile, renderView1)
# trace defaults for the display properties.
vtkFileDisplay.Representation = 'Outline'

# reset view to fit data
renderView1.ResetCamera()

# create a new 'TTK ContourForests'
tTKContourForests1 = TTKContourForests(Input=vtkFile)

# Properties modified on tTKContourForests1
tTKContourForests1.ArcSampling = 0
tTKContourForests1.ArcSmoothing = 100.0

# show data in view
tTKContourForests1Display = Show(tTKContourForests1, renderView1)
# trace defaults for the display properties.
tTKContourForests1Display.Representation = 'Surface'

# hide data in view
Hide(vtkFile, renderView1)

# show data in view
tTKContourForests1Display_1 = Show(OutputPort(tTKContourForests1, 1), renderView1)
# trace defaults for the display properties.
tTKContourForests1Display_1.Representation = 'Surface'

# hide data in view
Hide(vtkFile, renderView1)

# show data in view
tTKContourForests1Display_2 = Show(OutputPort(tTKContourForests1, 2), renderView1)
# trace defaults for the display properties.
tTKContourForests1Display_2.Representation = 'Outline'

# hide data in view
Hide(vtkFile, renderView1)

# hide data in view
Hide(tTKContourForests1, renderView1)

# hide data in view
Hide(tTKContourForests1, renderView1)

# hide data in view
Hide(OutputPort(tTKContourForests1, 2), renderView1)

# set active source
SetActiveSource(tTKContourForests1)

# get active source.
tTKContourForests1_1 = GetActiveSource()

# save data
SaveData(get_output_path(file_path, [VTP_EXTENSION]), proxy=OutputPort(tTKContourForests1_1, 1), DataMode='Ascii')

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitVertical(0, 0.5)

# set active view
SetActiveView(None)

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024L

# place view in the layout
layout1.AssignView(2, spreadSheetView1)

# show data in view
tTKContourForests1Display_3 = Show(OutputPort(tTKContourForests1, 1), spreadSheetView1)

# show data in view
tTKContourForests1Display_4 = Show(tTKContourForests1, spreadSheetView1)

# export view
nodes_file = get_output_path(file_path, [NODES_SUFFIX, CSV_EXTENSION])

ExportView(nodes_file, view=spreadSheetView1, FilterColumnsByVisibility=1)

# show data in view
tTKContourForests1Display_3 = Show(OutputPort(tTKContourForests1, 1), spreadSheetView1)

# export view
arcs_file = get_output_path(file_path, [ARCS_SUFFIX, CSV_EXTENSION])
ExportView(arcs_file, view=spreadSheetView1, FilterColumnsByVisibility=1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.0, 334.60652149512316]
renderView1.CameraParallelScale = 86.60254037844386

# Authors' code starts from here
# Author: Sushmitha/Adhitya

# Map node index to the function value
scalars = {}

# Map node index to node type
nodeType = {}

nodes = []

# Get bounds of VTK File
bounds = vtkFile.GetDataInformation().GetBounds()
[x_min,x_max,y_min,y_max,z_min,z_max]=bounds

# Get bounding box
x_dim = int(x_max - x_min + 1)
y_dim = int(y_max - y_min + 1)
z_dim = int(z_max - z_min + 1)

# Open the intermediate nodes file
with open(nodes_file, 'rb') as csvfile:
	# Pass over the header
	csvfile.readline() 
	spamreader = csv.reader(csvfile, delimiter=' ')
	
	# Iterate over the rows
	for r in spamreader:
		row = r[0].split(',')
		nodePosition = int(row[2])
		scalars[nodePosition] = float(row[0])
		ttkNodeType = int(row[3])

		# Convert TTK's node types to that of Recon
		if ttkNodeType == 0:
			nodeType[nodePosition] = 'MINIMA'
		elif ttkNodeType == 1 or ttkNodeType == 2 or ttkNodeType == 5:
			nodeType[nodePosition] = 'SADDLE'
		elif ttkNodeType == 3:
			nodeType[nodePosition] = 'MAXIMA'
		else:
			nodeType[nodePosition] = 'REGULAR' 
			
# Open the intermediate arcs file
with open(arcs_file, 'rb') as csvfile:
	# Pass over the header
	csvfile.readline()
	spamreader = csv.reader(csvfile, delimiter=' ')

	# Arcs file does not give out the node index
	# It gives out the relative x,y,z for each node
	# Every arc is stored in two rows
	for r in spamreader:
		row = r[0].split(',')
		x = int(row[3]) + int(abs(x_min))
		y = int(row[4]) + int(abs(y_min))
		z = int(row[5]) + int(abs(z_min))
		
		# Computer the node index
		index = z * x_dim * y_dim + y * x_dim + x
		nodes.append(index)

# Create the new RG File for the Contour Tree

rgfile = get_output_path(file_path, [RG_EXTENSION])
rgfile = open(rgfile, 'w')

# First line has number of nodes and arcs
rgfile.write(str(len(scalars)) + " " + str((len(nodes)/2)) + "\n")

# Write the Nodes first along with function value and node type
for i in scalars:
	rgfile.write(str(i) + " " + str(scalars[i]) + " " + nodeType[i] + "\n")

# Then write the Arcs
for index in range(0,len(nodes),2):
	rgfile.write(str(nodes[index]) + " " + str(nodes[index+1]) + "\n")

rgfile.close()

# Write an intermediate file just for the measure. Currently, this file is absolutely useless.
measure_path = get_output_path(file_path, [CSV_EXTENSION])
with open(measure_path, 'w') as csvfile:
	fieldnames = ['Node:0', 'Node:1', 'Scalar:0', 'Scalar:1', 'Type:0' , 'Type:1']
	writer = csv.writer(csvfile, delimiter=',')
	writer.writerow(fieldnames)	
	for index in range(0,len(nodes),2):
		writer.writerow([nodes[index], nodes[index+1], scalars[nodes[index]], scalars[nodes[index+1]], nodeType[nodes[index]], nodeType[nodes[index + 1]]])


# Visualize the tree as a dot file
contour_path = get_output_path(file_path, [DOT_EXTENSION])
contour_file = open(contour_path, 'w')

contour_file.write('graph {\n')
for index in range(0,len(nodes),2):
	line = str(nodes[index]) + ' -- ' + str(nodes[index+1])
	contour_file.write(line)
	contour_file.write('\n')
contour_file.write('}')
contour_file.close()

# Remove the intermediate files
os.remove(nodes_file)
os.remove(arcs_file)

print 'contour_tree_vtk.py Done! :)'

# Close Paraview instance
os._exit(0)
