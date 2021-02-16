# Python script to compute the clique number of a graph using NetworkX function.
# Input 1: Edge_file
"""
=================================================================================================
If you are using this code, kindly cite the following articles:
(1) A. Samal, H.K. Pharasi, S. J. Ramaia, H. Kannan, E. Saucan, J. Jost & A. Chakraborti, Network geometry and market instability, R. Soc. Open Sci. 8: 201734 (2021).
(2) A. Samal, S. Kumar, Y. Yadav & A. Chakraborti, Network-centric indicators for fragility in global financial indices, Front. Phys. 8: 624373 (2021).
=================================================================================================
"""

import networkx as nx
import numpy as np
import sys

infile = sys.argv[1]

G = nx.Graph()
G = nx.read_edgelist(infile, data = (('wt', float),))
print(nx.graph_clique_number(G))
