import csv, sys, os, re
from helper import *

# Send path of both VTK files as an arguments
file_path_1 = sys.argv[1]
file_path_2 = sys.argv[2]

# processCT does the individual work for each file
os.system('python processCT.py ' + file_path_1)
os.system('python processCT.py ' + file_path_2)

# Get the contour trees for the VTK files
contour_tree_measure_1 = get_file_name(file_path_1) + CSV_EXTENSION
contour_tree_measure_2 = get_file_name(file_path_2) + CSV_EXTENSION

# Get the difference measure [This is an extremely simple measure ~ Replace this file your own]
os.system('python measure.py ' + contour_tree_measure_1 + ' ' + contour_tree_measure_2)

# Get the VTP for visualization
contour_tree_vtp_1 = get_file_name(file_path_1, True) + VTP_EXTENSION
contour_tree_vtp_2 = get_file_name(file_path_2, True) + VTP_EXTENSION

# Replace the wildcards in visualizeGraphs to both the contour trees generated from above
file_replace('visualizeGraphs.py', WILDCARD_1, contour_tree_vtp_1)
file_replace('visualizeGraphs.py', WILDCARD_2, contour_tree_vtp_2)

# Run the script for visualizing the differences
os.system('paraview --script=visualizeGraphs.py')

# Replace the wildcard for next run
file_replace('contour_tree_vtk.py', contour_tree_vtp_1, WILDCARD_1)
file_replace('contour_tree_vtk.py', contour_tree_vtp_2, WILDCARD_2)
