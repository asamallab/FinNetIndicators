# Python script to compute the diameter of a weighted network using Networkx. 
# Note that weights represent distance along edges.
# Input 1: Edge_file with weights
"""
=================================================================================================
If you are using this code, kindly cite the following articles:
1) A. Samal, H.K. Pharasi, S. J. Ramaia, H. Kannan, E. Saucan, J. Jost & A. Chakraborti, Network geometry and market instability, R. Soc. Open Sci. 8: 201734 (2021).
2) A. Samal, S.Kumar, Y. Yadav & A. Chakraborti, Network-centric indicators for fragility in global financial indices, Front. Phys. 8: 624373 (2021).
=================================================================================================
"""

import networkx as nx
import sys

#read weighted edgelist
in_file = sys.argv[1]

G = nx.read_edgelist(in_file, comments='#',data=(('metric',float),))
G.remove_edges_from(nx.selfloop_edges(G))

#compute pairwise shortest path lengths using Dijkstra's algorithm
spl = nx.all_pairs_dijkstra_path_length(G, weight = 'metric')

eccentricity = {}
for source, lengths in spl:
	eccentricity[source] = max(lengths.values())

#Diameter
diameter = max(eccentricity.values())
print(str(diameter))
