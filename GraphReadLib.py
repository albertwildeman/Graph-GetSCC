import os
import numpy as np

def get_graph(filename):

    npy_version_exists = os.path.isfile(filename + ".npy")
    if not npy_version_exists:
        txt_to_npy(filename)

    return np.load(filename + ".npy")


def txt_to_npy(filename):

    filepath = os.getcwd() + "\\" + filename + ".txt"

    file_graph = open(filepath)

    nLines = sum(1 for line in file_graph)
    G = np.zeros((nLines, 2), dtype=np.int32)

    file_graph.seek(0,0)
    for iLine, line in enumerate(file_graph):
        G[iLine,0], G[iLine,1] = line.split(" ")[:2]

    file_graph.close()

    np.save(filename, G)

    return "done"
