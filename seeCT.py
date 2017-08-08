#### import the simple module from the paraview
from paraview.simple import *
import paraview.servermanager as SM

import os
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

file_path = '/home/raghavendra/Downloads/diffCT/data/output/tv_75-visual.vtp'
vtpFile = XMLPolyDataReader(FileName=[file_path])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [909, 548]

# show data in view
vtpFileDisplay = Show(vtpFile, renderView1)
# trace defaults for the display properties.
vtpFileDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera()

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=vtpFile)

# Properties modified on tTKSphereFromPoint1
tTKSphereFromPoint1.Radius = 0.15

# show data in view
tTKSphereFromPoint1Display = Show(tTKSphereFromPoint1, renderView1)
# trace defaults for the display properties.
tTKSphereFromPoint1Display.Representation = 'Surface'

# hide data in view
Hide(vtpFile, renderView1)

# set active source
SetActiveSource(vtpFile)

# show data in view
vtpFileDisplay = Show(vtpFile, renderView1)

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

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKSphereFromPoint1)

# Properties modified on threshold1
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
SetActiveSource(vtpFile)

# create a new 'Tube'
tube1 = Tube(Input=vtpFile)

# Properties modified on tube1
tube1.Vectors = [None, '']
tube1.Radius = 0.04

# show data in view
tube1Display = Show(tube1, renderView1)
# trace defaults for the display properties.
tube1Display.Representation = 'Surface'

# hide data in view
Hide(vtpFile, renderView1)

# set active source
SetActiveSource(vtpFile)

# show data in view
vtpFileDisplay = Show(vtpFile, renderView1)

# hide data in view
Hide(vtpFile, renderView1)

# show data in view
vtpFileDisplay = Show(vtpFile, renderView1)

# hide color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, False)

# Import a Colour Map specific for Critical Points display
ImportPresets(filename= 'CTNodeColourMap.json')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
nodeTypeLUT.ApplyPreset('CTNodeColourMap', True)

# get opacity transfer function/opacity map for 'NodeType'
nodeTypePWF = GetOpacityTransferFunction('NodeType')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
nodeTypePWF.ApplyPreset('CTNodeColourMap', True)

#change interaction mode for render view
renderView1.InteractionMode = '2D'

# current camera placement for renderView1
renderView1.CameraPosition = [1.5966980755329132, -0.017842769622802734, 18.758492643983434]
renderView1.CameraFocalPoint = [1.5966980755329132, -0.017842769622802734, -0.1044418215751648]
renderView1.CameraParallelScale = 4.882086686207304
