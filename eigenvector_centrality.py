# Python script to compute and print the eigenvector centrality of each node in a graph using Networkx.
# Input 1: Edge_file
# Input 2: Out_file containing the eigenvector centrality of each node 
"""
=================================================================================================
If you are using this code, kindly cite the following articles:
1) A. Samal, H.K. Pharasi, S. J. Ramaia, H. Kannan, E. Saucan, J. Jost & A. Chakraborti, Network geometry and market instability, (Submitted).
2) A. Samal, S.Kumar, Y. Yadav & A. Chakraborti, Network-centric indicators for fragility in global financial indices, (Submitted).
=================================================================================================
"""

import networkx as nx
import sys

in_file = sys.argv[1]
out_file = sys.argv[2]

f = open(out_file, 'w')

evc = nx.eigenvector_centrality_numpy(G,weight = 'metric')

for node, value in evc.items():
	f.write(str(node) + '\t' + str(value) + '\n')


