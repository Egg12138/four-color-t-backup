#Painter
"""
提供数个涂色方法
"""
from Graphy import GraphByVertex, Vertex
from numpy import random as rand
import algorithm.Random as ar
def RandGenAdj(max_v, max_deg):

	"""
	G = RandGenAdj(max_v, max_deg)
	max vertex  : 节点数
	max degree : 每个节点的最大度数（[1, max_deg]个)
	"""
	maxvset = set(list(range(max_v)))
	G = GraphByVertex(max_v, max_deg)
	for idx in range(max_v):
		G.addVertex(Vertex(idx, 0, []))

	for idx in range(max_v):
		degree_per_v = rand.randint(1, max_deg)#每个节点的邻接节点数， 0个到max_deg个
		tmp = {idx}

		for i in range(degree_per_v):
			w = ar.choicerest(tmp, maxvset)
			tmp.add(w)
			G.addEdge(idx, w)
		'''while len(G.get_edgesof(idx)) == 0: 
			w = ar.choicerest({idx}, maxvset)
			G.addEdge(idx, w)'''
	#print(f"{G.all_edges=}")
	#G.sort_by_degree()
	#print(f"{G.all_edges=}")
	print('\n')
	return G


def randfill(G:GraphByVertex):
	"""随机染色"""
	#Start the Process of filling
	for idx, clr in zip(G.G, rand.randint(1, 5, len(G))):
		G.set_colorof(idx.get_idx, clr)

def randGen_sort(max_v, max_deg):
	pass