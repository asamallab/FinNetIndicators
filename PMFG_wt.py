# Python script to generate a weighted PMFG from the correlation matrix in the form of edge list. 
# Reference for PMFG method: Tumminello M, Aste T, Di Matteo T, Mantegna RN. A tool for filtering information in complex systems. Proceedings of the National Academy of Sciences USA 102 (2005) 10421–10426. #doi:10.1073/pnas.0500298102.
# Input 1: Correlation matrix in form of edge list
# Input 2: Out_file
# Input 3: Node_file
"""
=================================================================================================
If you are using this code, kindly cite the following articles:
1) A. Samal, H.K. Pharasi, S. J. Ramaia, H. Kannan, E. Saucan, J. Jost & A. Chakraborti, Network geometry and market instability, (Submitted).
2) A. Samal, S.Kumar, Y. Yadav & A. Chakraborti, Network-centric indicators for fragility in global financial indices, (Submitted)
=================================================================================================
"""

import networkx as nx
import planarity
import itertools
import sys

in_file = sys.argv[1]
out_file = sys.argv[2]
node_file = sys.argv[3]

f = open(out_file,'w')
g = open(node_file, 'w') 

#Define sorting function used to sort edges in the graph in descending of correlation values
def sort_graph_edges(G):
    sorted_edges = []
    for source, dest, data in sorted(G.edges(data=True), key=lambda x: x[2]['corr'], reverse = True):
        sorted_edges.append((source, dest, data['metric']))
        
    return sorted_edges

#Function used to generate weighted PMFG
def compute_PMFG(sorted_edges, nb_nodes):
    PMFG = nx.Graph()
    for edge in sorted_edges:
        PMFG.add_edge(edge[0], edge[1], metric = edge[2])
        if not planarity.is_planar(PMFG):
            PMFG.remove_edge(edge[0], edge[1])
            
        if len(PMFG.edges()) == 3*(nb_nodes-2):
            break
    
    return PMFG


#Generate a graph from correlation values list and remove self loops
G = nx.read_edgelist(in_file,comments = '#', data = (('corr',float),('metric',float)))
G.remove_edges_from(G.selfloop_edges())

#Generate weighted PMFG
nb_nodes = G.number_of_nodes()
sorted_edges = sort_graph_edges(G)
PMFG = compute_PMFG(sorted_edges, nb_nodes)

#Write in output files
for item in PMFG.edges(data = 'metric'):
	f.write(str(item[0]) + '\t' + str(item[1]) + '\t' + str(item[2]) + '\n')

#Write in Node files
nodes = []
nodes = list(PMFG.nodes())
for node in nodes:
	g.write(node + '\n')



	

