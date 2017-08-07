#### import the simple module from the paraview
from paraview.simple import *
from helper import *

import os

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Random wildcards! Cannot pass arguments to this file
file_path1 = 'adhitya'
file_path2 = 'sushmitha'

# create a new 'XML PolyData Reader'
vtpFile1 = XMLPolyDataReader(FileName=[file_path1])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
vtpFile1Display = Show(vtpFile1, renderView1)
# trace defaults for the display properties.
vtpFile1Display.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera()

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitHorizontal(0, 0.5)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [452, 548]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.StereoType = 0
renderView2.Background = [0.32, 0.34, 0.43]

# place view in the layout
layout1.AssignView(2, renderView2)

# create a new 'XML PolyData Reader'
vtpFile2 = XMLPolyDataReader(FileName=[file_path2])

# show data in view
vtpFile2Display = Show(vtpFile2, renderView2)
# trace defaults for the display properties.
vtpFile2Display.Representation = 'Surface'

# reset view to fit data
renderView2.ResetCamera()

# set active source
SetActiveSource(vtpFile1)

# set active view
SetActiveView(renderView1)

# create a new 'Transform'
transform1 = Transform(Input=vtpFile1)

# Properties modified on transform1.Transform
############################################
transform1.Transform.Scale = [1, 1, 1]

# show data in view
transform1Display = Show(transform1, renderView1)
# trace defaults for the display properties.
transform1Display.Representation = 'Surface'

# hide data in view
Hide(vtpFile1, renderView1)

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(vtpFile2)

# Get bounds of VTK File1
bounds1 = vtpFile1.GetDataInformation().GetBounds()
[x_min1,x_max1,y_min1,y_max1,z_min1,z_max1]=bounds1

# Get bounding box
x_dim1 = float(x_max1 - x_min1 + 1)
y_dim1 = float(y_max1 - y_min1 + 1)
z_dim1 = float(z_max1 - z_min1 + 1)

# Get bounds of VTK File2
bounds2 = vtpFile2.GetDataInformation().GetBounds()
[x_min2,x_max2,y_min2,y_max2,z_min2,z_max2]=bounds2

# Get bounding box
x_dim2 = float(x_max2 - x_min2 + 1)
y_dim2 = float(y_max2 - y_min2 + 1)
z_dim2 = float(z_max2 - z_min2 + 1)

# create a new 'Transform'
transform2 = Transform(Input=vtpFile2)


###########################################
# Properties modified on transform2.Transform
# Adhitya: Make the dimensions of one equal to the other
transform2.Transform.Scale = [x_dim1/x_dim2, y_dim1/y_dim2, z_dim1/z_dim2]

# show data in view
transform2Display = Show(transform2, renderView2)
# trace defaults for the display properties.
transform2Display.Representation = 'Surface'

# hide data in view
Hide(vtpFile2, renderView2)

# set active view
SetActiveView(renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# set active view
SetActiveView(renderView2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(transform1)

# set active view
SetActiveView(renderView2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(transform2)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(transform1)

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=transform1)

# Properties modified on tTKSphereFromPoint1
tTKSphereFromPoint1.Radius = 0.15

# show data in view
tTKSphereFromPoint1Display = Show(tTKSphereFromPoint1, renderView1)
# trace defaults for the display properties.
tTKSphereFromPoint1Display.Representation = 'Surface'

# hide data in view
Hide(transform1, renderView1)

# set active source
SetActiveSource(transform1)

# show data in view
transform1Display = Show(transform1, renderView1)

# hide data in view
Hide(transform1, renderView1)

# set active source
SetActiveSource(tTKSphereFromPoint1)

# set scalar coloring
ColorBy(tTKSphereFromPoint1Display, ('POINTS', 'NodeType'))

# rescale color and/or opacity maps used to include current data range
tTKSphereFromPoint1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tTKSphereFromPoint1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'NodeType'
nodeTypeLUT = GetColorTransferFunction('NodeType')

# set active source
SetActiveSource(transform1)

# set active source
SetActiveSource(tTKSphereFromPoint1)

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKSphereFromPoint1)

# Properties modified on threshold1
# Adhitya: Do not display all Bent nodes [Bent nodes have a node type of 0]
threshold1.ThresholdRange = [1.0, 6.0]

# show data in view
threshold1Display = Show(threshold1, renderView1)
# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'

# hide data in view
Hide(tTKSphereFromPoint1, renderView1)

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# hide color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, False)

# set active source
SetActiveSource(transform1)

# create a new 'Tube'
tube1 = Tube(Input=transform1)

# Properties modified on tube1
tube1.Vectors = [None, '']
tube1.Radius = 0.04

# show data in view
tube1Display = Show(tube1, renderView1)
# trace defaults for the display properties.
tube1Display.Representation = 'Surface'

# hide data in view
Hide(transform1, renderView1)

# create a new 'Threshold'
threshold2 = Threshold(Input=tube1)

# Properties modified on threshold2
# Adhitya: This is not the best way to do this.
# Use a threshold to display all tubes between 6 and 7 [All arcs connecting missing nodes]
threshold2.ThresholdRange = [5.9, 7.0]

# show data in view
threshold2Display = Show(threshold2, renderView1)
# trace defaults for the display properties.
threshold2Display.Representation = 'Surface'

# hide data in view
Hide(tube1, renderView1)

# change solid color
threshold2Display.DiffuseColor = [1.0, 1.0, 0.0]

# set active source
SetActiveSource(tube1)

# show data in view
tube1Display = Show(tube1, renderView1)

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(vtpFile2)

# set active source
SetActiveSource(transform2)

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=transform2)

# Properties modified on tTKSphereFromPoint2
tTKSphereFromPoint2.Radius = 0.15

# show data in view
tTKSphereFromPoint2Display = Show(tTKSphereFromPoint2, renderView2)
# trace defaults for the display properties.
tTKSphereFromPoint2Display.Representation = 'Surface'

# hide data in view
Hide(transform2, renderView2)

# set active source
SetActiveSource(transform2)

# set active source
SetActiveSource(tTKSphereFromPoint2)

# create a new 'Threshold'
threshold3 = Threshold(Input=tTKSphereFromPoint2)

# Properties modified on threshold3
# Adhitya: Do not display all Bent nodes [Bent nodes have a node type of 0]
threshold3.ThresholdRange = [1.0, 6.0]

# show data in view
threshold3Display = Show(threshold3, renderView2)
# trace defaults for the display properties.
threshold3Display.Representation = 'Surface'

# hide data in view
Hide(tTKSphereFromPoint2, renderView2)

# set active source
SetActiveSource(tTKSphereFromPoint2)

# set active source
SetActiveSource(transform2)

# create a new 'Tube'
tube2 = Tube(Input=transform2)

# Properties modified on tube2
tube2.Vectors = [None, '']
tube2.Radius = 0.04

# show data in view
tube2Display = Show(tube2, renderView2)
# trace defaults for the display properties.
tube2Display.Representation = 'Surface'

# hide data in view
Hide(transform2, renderView2)

# create a new 'Threshold'
threshold4 = Threshold(Input=tube2)

# Properties modified on threshold4
# Adhitya: This is not the best way to do this.
# Use a threshold to display all tubes between 6 and 7 [All arcs connecting missing nodes]
threshold4.ThresholdRange = [5.9, 7.0]

# show data in view
threshold4Display = Show(threshold4, renderView2)
# trace defaults for the display properties.
threshold4Display.Representation = 'Surface'

# hide data in view
Hide(tube2, renderView2)

# change solid color
threshold4Display.DiffuseColor = [1.0, 1.0, 0.0]

# set active source
SetActiveSource(tube2)

# show data in view
tube2Display = Show(tube2, renderView2)

# set active source
SetActiveSource(tTKSphereFromPoint2)

# set active source
SetActiveSource(threshold3)

# set scalar coloring
ColorBy(threshold3Display, ('POINTS', 'NodeType'))

# rescale color and/or opacity maps used to include current data range
threshold3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
threshold3Display.SetScalarBarVisibility(renderView2, True)

# hide color bar/color legend
threshold3Display.SetScalarBarVisibility(renderView2, False)

# Import a Colour Map specific for Critical Points display
ImportPresets(filename= 'CTNodeColourMap.json')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
nodeTypeLUT.ApplyPreset('CTNodeColourMap', True)

# get opacity transfer function/opacity map for 'NodeType'
nodeTypePWF = GetOpacityTransferFunction('NodeType')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
nodeTypePWF.ApplyPreset('CTNodeColourMap', True)

# set active view
SetActiveView(renderView1)

#change interaction mode for render view
renderView1.InteractionMode = '2D'

# set active view
SetActiveView(renderView2)

#change interaction mode for render view
renderView2.InteractionMode = '2D'

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(renderView2)

# set active view
SetActiveView(renderView1)

#### saving camera placements for all active views
# current camera placement for renderView2
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [4.58231120011033, -50.15802711959017, 911.4977077946097]
renderView2.CameraFocalPoint = [4.58231120011033, -39.77388976851554, 5.865034696979825]
renderView2.CameraViewUp = [0.0, 0.9999342699645772, 0.011465415404949008]
renderView2.CameraParallelScale = 6.335127753982459

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [4.58231120011033, -50.15802711959017, 911.4977077946097]
renderView1.CameraFocalPoint = [4.58231120011033, -39.77388976851554, 5.865034696979825]
renderView1.CameraViewUp = [0.0, 0.9999342699645771, 0.011465415404949006]
renderView1.CameraParallelScale = 6.335127753982459

paraview.simple.AddCameraLink(renderView1, renderView2, 'Camera Link')
