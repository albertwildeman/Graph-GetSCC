import numpy as np

def kosaraju(G):

    # Shift node numbers to start at 0
    G -= G.min()

    # Calculate finishing time for each node, that is, the order is in which the second, forward, DFS loop will execute
    f = kosaraju_rev_dfs_loop(G)

    leaders = kosaraju_fwd_dfs_loop(G, f)

    return leaders

def kosaraju_rev_dfs_loop(G):
    # Perform the first DFS (depth-first search) loop on the reverse of graph G

    # t is a counter that marks number of already-explored nodes.
    # It will be used to determine the processing order of the nodes for the
    # second (forward) DFS loop.
    t = 0

    # Get number of nodes from edge list G
    nNodes = G.max() + 1

    # initialize array that will hold the finishing times of all nodes
    f = np.zeros(nNodes, dtype=np.int32)

    # Initialize an array to keep track of which nodes have been explored
    explored = np.zeros(nNodes, dtype=np.bool)

    for iNode in range(nNodes):
        if not explored[iNode]:
            # call DFS, but with the rows (ie, direction) of the edge list reversed
            t = DFS_rev(G[:, ::-1], iNode, t, f, explored)

    return f

def DFS_rev(G, s, t, f, explored):

    explored[s] = True

    edges_from_s = G[G[:,0]==s][:,1]
    for targetNode in edges_from_s:
        if not explored[targetNode]:
            t = DFS_rev(G, targetNode, t, f, explored)

    # Set finishing time for node just explored to the current "time" t
    f[s] = t
    # Increment t
    t += 1
    print("t: " + str(t))
    return t

def kosaraju_fwd_dfs_loop(G, f):
    # Perform the second DFS (depth-first search) loop on the graph G

    # t is a counter that marks number of already-explored nodes.
    # It will be used to determine the processing order of the nodes for the
    # second (forward) DFS loop.
    t = 0

    # # Get number of nodes from edge list G
    # nNodes = G.max() + 1
    #
    # # initialize array that will hold the finishing times of all nodes
    # f = np.zeros(nNodes, dtype=np.int32)
    #
    # # Initialize an array to keep track of which nodes have been explored
    # explored = np.zeros(nNodes, dtype=np.bool)
    #
    # for iNode in range(nNodes):
    #     if not explored[iNode]:
    #         # call DFS, but with the rows (ie, direction) of the edge list reversed
    #         DFS_fwd(G[:, ::-1], iNode, t, f, explored)

    return leaders

