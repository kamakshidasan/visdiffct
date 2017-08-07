import os, re

# List of constants
CSV_EXTENSION = '.csv'
RG_EXTENSION = '.rg'
TXT_EXTENSION = '.txt'
VTP_EXTENSION = '.vtp'
DOT_EXTENSION = '.dot'

GRAPH_SUFFIX = '-graph'
VISUAL_SUFFIX = '-visual'

TREE_SUFFIX = '-tree'
NODES_SUFFIX = '-nodes'
ARCS_SUFFIX = '-arcs'

WILDCARD_1 = 'adhitya'
WILDCARD_2 = 'sushmitha'

INPUT_FOLDER = 'input'
OUTPUT_FOLDER = 'output'

# Create types for new node types
MISSING_NODE = 6
MISSING_BEND_NODE = 7
INITIAL_BEND_NODE = 0


# Replace a wildcard in a file
def file_replace(fname, pat, s_after):
    # first, see if the pattern is even in the file.
    with open(fname) as f:
        if not any(re.search(pat, line) for line in f):
            return # pattern does not occur in file so we are done.

    # pattern is in the file, so perform replace operation.
    with open(fname) as f:
        out_fname = fname + ".tmp"
        out = open(out_fname, "w")
        for line in f:
            out.write(re.sub(pat, s_after, line))
        out.close()
        os.rename(out_fname, fname)

# Return the just the name when path is False
# Return the name appended with the parent path when path is True
def get_file_name(file_path, path = False):
	file_name = os.path.splitext(os.path.basename(file_path))[0]
	parent_path = get_parent_path(file_path)
	if path:
		return join_file_path(parent_path, file_name)
	else:
		return file_name

def get_file_extension(file_path):
	file_basename = os.path.basename(file_path)
	file_text = os.path.splitext(file_basename)
	return file_text[1]

def get_parent_path(file_path):
	return os.path.abspath(os.path.join(file_path, os.pardir))

def get_input_path(file_path):
	return os.path.join(get_parent_path(file_path), INPUT_FOLDER)

def get_output_path(file_path, arguments, output_folder = True):
	output_path = os.path.join(get_parent_path(file_path), OUTPUT_FOLDER)

	if output_folder == False:
		output_path = get_parent_path(file_path)

	output_path = os.path.join(output_path, get_file_name(file_path))

	for argument in arguments:
		output_path += argument

	return output_path
	

def join_file_path(file_path, file_name):
	return os.path.join(file_path, file_name)
