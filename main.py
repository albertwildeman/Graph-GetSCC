import numpy as np

from GraphReadLib import get_graph
from KosarajuLib import kosaraju

#  Get the graph from file
# SCC_filename = "SCCsmall"
SCC_filename = "SCCsmall"
G = get_graph(SCC_filename)

# Perform the Kosaraju algorithm to get the leaders for each node.
# (the nodes reporting a shared leader will belong to the same SCC).
leaders = kosaraju(G)

print('all done.')
