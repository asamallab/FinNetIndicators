# Python script to compute the global reaching centrality of a weighted, undirected graph.
# Reference for global reaching centrality: Mones E, Vicsek L, Vicsek T. Hierarchy measure for complex networks. PLoS One 7 (2012) 1–10.352.
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

#generalization of closeness centrality for disconnected graphs (Opsahl)
#Here weight of the edges is interpreted as distance and hence I have directly used Dijkstra's
#algorithm without inverting the weights (Newman(2001), Brandes(2001), Opsahl(2010)) 
def weighted_closeness_centrality(G,v,weight):
	shortest_path_lengths = nx.single_source_dijkstra_path_length(G,v,weight = weight)
	del shortest_path_lengths[v]
	return sum(np.reciprocal(list(shortest_path_lengths.values())))


#Global reaching centrality for weighted, undirected networks 
# Mones et. al (2012)
def weighted_undirected_grc(G,weight):
	closeness_centralities = [weighted_closeness_centrality(G,v = node,weight = weight) for node in G.nodes()]
	max_cc = max(closeness_centralities)
	differences = [(max_cc - item) for item in closeness_centralities]
	N = len(G)
	return sum(differences)/((N-1)*(N-1))


#begin computing GRC
in_file = sys.argv[1]

G = nx.read_edgelist(in_file, comments='#',data=(('metric',float),))
G.remove_edges_from(nx.selfloop_edges(G))

print(str(weighted_undirected_grc(G, weight = 'metric')))







