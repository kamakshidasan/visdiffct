import csv, sys, os, re
from helper import *

# Send path of both VTK files as an arguments
file_path_1 = sys.argv[1]
file_path_2 = sys.argv[2]

# Create output folder
create_output_folder(file_path_1)

# processCT does the individual work for each file
run_python_script('processCT.py', [file_path_1])
run_python_script('processCT.py', [file_path_2])

# Get the contour trees for the VTK files
contour_tree_measure_1 = get_output_path(file_path_1, [CSV_EXTENSION])
contour_tree_measure_2 = get_output_path(file_path_2, [CSV_EXTENSION])

# Get the difference measure [This is an extremely simple measure ~ Replace this file your own]
# Ideally this should spit out a missing_nodes.txt file
# In this example, we have defined it
run_python_script('measure.py', [contour_tree_measure_1, contour_tree_measure_2])

# From the coordinates make a VTP file
coordinates_1 = get_output_path(file_path_1, [TXT_EXTENSION])
coordinates_2 = get_output_path(file_path_2, [TXT_EXTENSION])

run_python_script('makeVTPfromRG.py', [coordinates_1])
run_python_script('makeVTPfromRG.py', [coordinates_2, 'data/missing_nodes.txt'])

# Get the VTP for visualization
contour_tree_vtp_1 = get_output_path(file_path_1, [VISUAL_SUFFIX, VTP_EXTENSION])
contour_tree_vtp_2 = get_output_path(file_path_2, [VISUAL_SUFFIX, VTP_EXTENSION])

# Replace the wildcards in visualizeDiff to both the contour trees generated from above
replace_wildcard('visualizeDiff.py', WILDCARD_1, contour_tree_vtp_1)
replace_wildcard('visualizeDiff.py', WILDCARD_2, contour_tree_vtp_2)

# Run the script for visualizing the differences
run_paraview_script('visualizeDiff.py')

# Replace the wildcard for next run
replace_wildcard('visualizeDiff.py', contour_tree_vtp_1, WILDCARD_1)
replace_wildcard('visualizeDiff.py', contour_tree_vtp_2, WILDCARD_2)

'''
# If you want to look at a single CT
replace_wildcard('seeCT.py', WILDCARD_1, contour_tree_vtp_1)
run_paraview_script('seeCT.py')
replace_wildcard('seeCT.py', contour_tree_vtp_1, WILDCARD_1)
'''

delete_output_folder(file_path_1)
