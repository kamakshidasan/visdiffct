import sys
import os
from writeNodesEdges import writeObjects
from helper import *

# Get branch decomposition of CT from Recon
# First line has the number of nodes and edges
# Then the list of edges
# Followed by nodes [node-index, node-position, scalar-function, node-type, x, y, z]
branch_file = sys.argv[1]

file_name = get_file_name(branch_file)

branchfile = open(branch_file, 'rb')

# Get number of nodes and edges
[node_count, edge_count] = map(int, branchfile.readline().strip().split(" "))

# List of tuples
edges = []

# List of lists of x, y, z
positions = []

# List of function values
scalars = []

# List of node types
types = []

# Adjacency list
connections = {}

# Read missing nodes from file
try:
	missing_nodes_file = sys.argv[2]
	with open(missing_nodes_file) as f:
		missing_nodes = f.readlines()
	missing_nodes = [int(node.strip()) for node in missing_nodes]
except IndexError:
	missing_nodes = []

# Iterate through edges
for i in range(0, edge_count):
	edge = tuple(map(int, branchfile.readline().strip().split(" ")))
	edges.append(edge)
	
# Sometimes you can get more number of nodes in the first line during simplification from Recon
# ToDo: Check what is going on

# Iterate through nodes
for line in branchfile:
	node = line.strip().split(" ")

	# Map node properties to respective arrays
	node_index = int(node[0])
	node_position = int(node[1])
	scalar_value = float(node[2])
	node_type = int(node[3])
	
	node_x = float(node[4])
	node_y = float(node[5])
	node_z = float(node[6])
	
	positions.append([node_x, node_y, node_z])
	scalars.append(scalar_value)
	types.append(node_type)
	
# Create Adjacency List
for node_1, node_2 in edges:
	if node_1 not in connections.keys():
		connections[node_1] = []
	if node_2 not in connections.keys():
		connections[node_2] = []

	connections[node_1].append(node_2)
	connections[node_2].append(node_1)

# Iterate through each of the missing nodes
for node in missing_nodes:
	# Assign missing node type
	types[node] = MISSING_NODE
	
	# Process nodes connected to the missing nodes
	for i in connections[node]:
		# If node is initially bent, mark to be missing now
		if(types[i] == INITIAL_BEND_NODE):
			types[i] = MISSING_BEND_NODE
			# Mark all nodes connected to the bent node to be missing
			for connects in connections[i]:
				types[connects] = MISSING_NODE
		# For all the node types, mark as missing
		else:
			types[i] = MISSING_NODE

# Make VTP file from processed data
writeObjects(positions, edges=edges, scalar= scalars, name = 'scalars', scalar2 = types, name2 = 'NodeType', fileout = get_output_path(branch_file, [VISUAL_SUFFIX], False))

os.remove(branch_file)
#branchfile.close()

print 'makeVTPfromRG.py Done! :)'
