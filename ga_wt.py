# Python script to compute the Global assortativty of weighted networks.
# Reference for Global assoratativity: C.C. Leung, H.F. Chau, Weighted assortative and disassortative networks model, Physica A, 378: 591-602 (2007). 
# Input 1: Edge_file with strengths	
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

G = nx.read_edgelist(in_file, comments='#',data=(('strength',float),))
G.remove_edges_from(nx.selfloop_edges(G))

#start computing assortativity 
first_term = 0
second_term = 0
third_term = 0
H = 0  #total link weight
for source, target, dist in G.edges.data():
	j = G.degree(source)
	k = G.degree(target) 
	H = H + dist['strength']   
	first_term = first_term + (dist['strength']*j*k) 
	second_term = second_term + (dist['strength']*(j+k)) 
	third_term = third_term + (dist['strength']*(j*j + k*k)) 

first_term = first_term/H
third_term = third_term/(2*H)

second_term = second_term/(2*H)
second_term = second_term*second_term

GA = (first_term - second_term)/(third_term - second_term)

print(str(GA))
