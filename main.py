import numpy as np

from GraphReadLib import get_graph
from KosarajuLib import kosaraju

#  Get the graph from file
# SCC_filename = "SCCsmall"
# SCC_filename = "SCCsmall2"
SCC_filename = "SCC"
G = get_graph(SCC_filename)

if SCC_filename != "SCC":
    sortOrder = np.argsort(G[:,0])
    G = G[sortOrder,:]

# Perform the Kosaraju algorithm to get the leaders for each node.
# (the nodes reporting a shared leader will belong to the same SCC).
leaders = kosaraju(G)
nLeaders = leaders.max()+1
SCC_sizes = np.zeros(nLeaders,dtype=np.int32)

for ldr in range(nLeaders):
    SCC_sizes[ldr] = sum(leaders==ldr)

SCC_sizes[::-1].sort()
print("Size of largest 5 SCCs: " + str(SCC_sizes[:5]))


print('all done.')
