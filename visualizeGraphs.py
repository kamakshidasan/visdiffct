#### import the simple module from the paraview
from paraview.simple import *
from helper import *
import os

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML PolyData Reader'

# Random wildcards! Cannot pass arguments to this file
file_name1 = '/home/raghavendra/Downloads/diffCTtv_0-graph-visual'
file_name2 = '/home/raghavendra/Downloads/diffCTtv_75-graph-visual'

file_path1 = os.getcwd() + os.sep + file_name1
file_path2 = os.getcwd() + os.sep + file_name2

parent_path = os.getcwd() + os.sep 

vtpFile1 = XMLPolyDataReader(FileName=[file_path1])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
vtpFile1Display = Show(vtpFile1, renderView1)
# trace defaults for the display properties.
vtpFile1Display.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera()

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=vtpFile1)

# Properties modified on tTKSphereFromPoint1
tTKSphereFromPoint1.Radius = 0.15

# show data in view
tTKSphereFromPoint1Display = Show(tTKSphereFromPoint1, renderView1)
# trace defaults for the display properties.
tTKSphereFromPoint1Display.Representation = 'Surface'

# hide data in view
Hide(vtpFile1, renderView1)

# set scalar coloring
ColorBy(tTKSphereFromPoint1Display, ('POINTS', 'NodeType'))

# rescale color and/or opacity maps used to include current data range
tTKSphereFromPoint1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tTKSphereFromPoint1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'NodeType'
nodeTypeLUT = GetColorTransferFunction('NodeType')

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKSphereFromPoint1)

# Properties modified on threshold1
# Do not display all Bent nodes [Bent nodes have a node type of 0]
threshold1.ThresholdRange = [1.0, 6.0]

# show data in view
threshold1Display = Show(threshold1, renderView1)
# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'

# hide data in view
Hide(tTKSphereFromPoint1, renderView1)

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(tTKSphereFromPoint1)

# show data in view
tTKSphereFromPoint1Display = Show(tTKSphereFromPoint1, renderView1)

# show color bar/color legend
tTKSphereFromPoint1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(tTKSphereFromPoint1, renderView1)

# set active source
SetActiveSource(vtpFile1)

# show data in view
vtpFile1Display = Show(vtpFile1, renderView1)

# create a new 'Tube'
tube1 = Tube(Input=vtpFile1)

# Properties modified on tube1
tube1.Vectors = [None, '']
tube1.Radius = 0.04

# show data in view
tube1Display = Show(tube1, renderView1)
# trace defaults for the display properties.
tube1Display.Representation = 'Surface'

# hide data in view
Hide(vtpFile1, renderView1)

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

#change interaction mode for render view
renderView1.InteractionMode = '2D'

# set active source
SetActiveSource(vtpFile1)

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

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=vtpFile2)

# Properties modified on tTKSphereFromPoint2
tTKSphereFromPoint2.Radius = 0.15

# show data in view
tTKSphereFromPoint2Display = Show(tTKSphereFromPoint2, renderView2)
# trace defaults for the display properties.
tTKSphereFromPoint2Display.Representation = 'Surface'

# hide data in view
Hide(vtpFile2, renderView2)

# set scalar coloring
ColorBy(tTKSphereFromPoint2Display, ('POINTS', 'NodeType'))

# rescale color and/or opacity maps used to include current data range
tTKSphereFromPoint2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tTKSphereFromPoint2Display.SetScalarBarVisibility(renderView2, True)

# create a new 'Threshold'
threshold3 = Threshold(Input=tTKSphereFromPoint2)

# Properties modified on threshold3
# Do not display all Bent nodes [Bent nodes have a node type of 0]
threshold3.ThresholdRange = [1.0, 6.0]

# show data in view
threshold3Display = Show(threshold3, renderView2)
# trace defaults for the display properties.
threshold3Display.Representation = 'Surface'

# hide data in view
Hide(tTKSphereFromPoint2, renderView2)

# show color bar/color legend
threshold3Display.SetScalarBarVisibility(renderView2, True)

# set active source
SetActiveSource(vtpFile2)

# show data in view
vtpFile2Display = Show(vtpFile2, renderView2)

# create a new 'Tube'
tube2 = Tube(Input=vtpFile2)

# Properties modified on tube2
tube2.Vectors = [None, '']
tube2.Radius = 0.04

# show data in view
tube2Display = Show(tube2, renderView2)
# trace defaults for the display properties.
tube2Display.Representation = 'Surface'

# hide data in view
Hide(vtpFile2, renderView2)

# create a new 'Threshold'
threshold4 = Threshold(Input=tube2)

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

#change interaction mode for render view
renderView2.InteractionMode = '2D'

# set active source
SetActiveSource(tTKSphereFromPoint2)

# Import a Colour Map specific for Critical Points display
ImportPresets(filename= parent_path + 'CTNodeColourMap.json')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
nodeTypeLUT.ApplyPreset('CTNodeColourMap', True)

# get opacity transfer function/opacity map for 'NodeType'
nodeTypePWF = GetOpacityTransferFunction('NodeType')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
nodeTypePWF.ApplyPreset('CTNodeColourMap', True)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [7.300515492812336, -7.569525679170328, 69.81633455028873]
renderView1.CameraFocalPoint = [7.300515492812336, -7.569525679170328, 4.315968871116638]
renderView1.CameraParallelScale = 9.569380957781997


# current camera placement for renderView2
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [7.300515492812336, -7.569525679170328, 69.81633455028873]
renderView2.CameraFocalPoint = [7.300515492812336, -7.569525679170328, 4.315968871116638]
renderView2.CameraParallelScale = 9.569380957781997

paraview.simple.AddCameraLink(renderView1, renderView2, 'Camera Link')
