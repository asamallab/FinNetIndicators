# FinNetIndicators

The codes/scripts in the 'FinNetIndicators' repository can be used to filter cross-correlation matrices to construct network based on two methods: <br/>
(a) Minimum spanning tree (MST) +  Threshold <br/>
(b) Planar Maximally Filtered Graph (PMFG) 

Thereafter, the filtered network in the form of edge list or file can be characterized by computing several network measures including edge-based measures. <br/>
The codes/scripts require input file in the form of edge lists. <br/>
FormanUndirected.cpp also requires an input file containing the list of nodes in the network.

These codes were written while carrying out research reported in the following manuscripts:
=================================================================================================
[1] A. Samal, H.K. Pharasi, S. J. Ramaia, H. Kannan, E. Saucan, J. Jost & A. Chakraborti, Network geometry and market instability, (Submitted). <br/>
[2] A. Samal, S.Kumar, Y. Yadav & A. Chakraborti, Network-centric indicators for fragility in global financial indices, (Submitted). <br/>
[3] S. Venkatesan, R.P. Vivek-Ananth, R.P. Sreejith, P. Mangalapandi, A.A. Hassanali & A. Samal, Network approach towards understanding the crazing in glassy amorphous polymers, Journal of Statistical Mechanics: Theory and Experiment 043305 (2018). <br/>
[4] A. Samal, R.P. Sreejith, J. Gu, S. Liu, E. Saucan & J. Jost, Comparative analysis of two discretizations of Ricci curvature for complex networks, Scientific Reports 8: 8650 (2018). <br/>
[5] R.P. Sreejith, K. Mohanraj, J. Jost, E. Saucan & A. Samal, Forman curvature for complex networks, Journal of Statistical Mechanics: Theory and Experiment 063206 (2016).

Please cite the above manuscripts if you use the codes in this repository for your work.

Code/Script Details:
=================================================

The following two scripts can be used to filter the cross-correlation matrices and generate edge files and node files of the filtered networks:
1) mst_wt.py : Python script to generate a weighted or unweighted filtered minimum spanning tree + thresholded network from the weighted network of cross-correlation values. The weights are interpreted as distances (costs).
2) PMFG_wt.py: Python script to generate a weighted PMFG from the weighted network of cross-correlation values. The weights are interpreted as distances (costs).

The following scripts can be used to compute the different network measures for the filtered networks:
1) clique_number.py : Clique number
2) diameter_wt.py: Diameter of a weighted network
3) eigenvector_centality.py : Eigenvector centrality for all the nodes of a weighted network
4) FormanUndirected.cpp: Forman-Ricci curvature for all the edges of a weighted/unweighted network 
5) ga_wt: Global assortativity of a weighted network
6) graph_measures.py : Number of edges, Average degree, Average Weighted Degree, Edge Density, Average Clustering coefficient
7) grc_wt_undir.py : Global Reaching Centrality of a weighted network
8) network_entropy.py : Entropy of an unweighted network
9) comm_eff.py : Communication efficiency of a weighted network
10) OR-UnDir.py : Ollivier-Ricci curvature for all the edges of a weighted/unweighted but undirected network
11) MengerHaantjesUnweighted.py : Menger-curvature and Haantjes-curvature for all the edges of an unweighted network


Example Folder:
=================================================================================================

The Example folder contains an already filtered example network which can be used to compute the different network measures.
Details of files:
1) example_distance.txt : Edge file with weights as distances
Note that we use this edge file to compute the diameter, global reaching centrality, communication efficiency, Forman-Ricci curvature, Ollivier-Ricci curvature, Menger-Ricci and Haantjes-Ricci curvature.
2) example_strength.txt : Edge file with weights as strengths
Note that we use this edge file to compute the eigenvector centrality, global assortativity and average weighted degree.
Any of the above two edge files can be used to compute clique number, average degree, edge density, average clustering coefficient and network entropy.
3) example_nodes.txt : Node file

The outputs of the computation of eigenvector centrality, Forman-Ricci curvature and Ollivier-Ricci curvature are also provided in the Example folder for replication.
