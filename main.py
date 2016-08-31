import numpy as np

from GraphReadLib import txt_to_ndarray

SCC_filename = "SCC.txt"

G = txt_to_ndarray(SCC_filename)
print(G)
