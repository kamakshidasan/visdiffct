import fileinput
import re
import os
import sys

from helper import *

# Send path of VTK file as an argument
file_path = sys.argv[1]
file_name = get_file_name(file_path)
file_extension = get_file_extension(file_path)

# Get the parent path
parent_path = get_parent_path(file_path)

# Replace wildcard ~ Paraview does not take in arguments for scripts
replace_wildcard('contour_tree_vtk.py', WILDCARD_1, file_path)

# Get Contour Tree in RG format from Paraview using TTK
run_paraview_script('contour_tree_vtk.py')

# Run modified Recon to give out coordinates
run_jar('recon.jar', [get_output_path(file_path, [RG_EXTENSION]), get_output_path(file_path, [TXT_EXTENSION])])

# Replace the wildcard for next run
replace_wildcard('contour_tree_vtk.py', file_path, WILDCARD_1)

print 'processCT.py Done! :)'
