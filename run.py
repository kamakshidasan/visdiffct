import csv, sys, os, re
from helper import *

# Send path of both VTK files as an arguments
file_path_1 = sys.argv[1]
file_path_2 = sys.argv[2]

# processCT does the individual work for each file
os.system('python processCT.py ' + file_path_1)
os.system('python processCT.py ' + file_path_2)

# Get the contour trees for the VTK files
contour_tree_measure_1 = get_output_path(file_path_1, [CSV_EXTENSION])
contour_tree_measure_2 = get_output_path(file_path_2, [CSV_EXTENSION])

# Get the difference measure [This is an extremely simple measure ~ Replace this file your own]
# Ideally this should spit out a missing_nodes.txt file
# In this example, we have defined it
os.system('python measure.py ' + contour_tree_measure_1 + ' ' + contour_tree_measure_2)

# From the coordinates make a VTP file
coordinates_1 = get_output_path(file_path_1, [TXT_EXTENSION])
coordinates_2 = get_output_path(file_path_2, [TXT_EXTENSION])

os.system('python makeVTPfromRG.py '+ coordinates_1)
os.system('python makeVTPfromRG.py '+ coordinates_2 + ' missing_nodes.txt')

# Get the VTP for visualization
contour_tree_vtp_1 = get_output_path(file_path_1, [VISUAL_SUFFIX, VTP_EXTENSION])
contour_tree_vtp_2 = get_output_path(file_path_2, [VISUAL_SUFFIX, VTP_EXTENSION])

# Replace the wildcards in visualizeGraphs to both the contour trees generated from above
file_replace('visualizeGraphs.py', WILDCARD_1, contour_tree_vtp_1)
file_replace('visualizeGraphs.py', WILDCARD_2, contour_tree_vtp_2)

# Run the script for visualizing the differences
os.system('paraview --script=visualizeGraphs.py')

# Replace the wildcard for next run
file_replace('visualizeGraphs.py', contour_tree_vtp_1, WILDCARD_1)
file_replace('visualizeGraphs.py', contour_tree_vtp_2, WILDCARD_2)
