
from algorithm.Travel import *
from collections import abc
from Graphy import GraphByVertex, Vertex, choice
from numpy import random as rand
import cProfile
from memory_profiler import *
import numpy as np
import sys

"""
现在已经有了一个随机生成连接情况的图
下一步是上色。
最后可视化就再说了吧。

"""


colors = ['red', 'yellow', 'blue', 'green']#Enumeration...

def RandGenAdj(max_v, max_deg):

	"""
	max vertex  : max number of vertexes to be generated
	max degree : max number of linked vertex a vertex can have
	"""
	maxvset = set(list(range(max_v)))
	G = GraphByVertex()
	for idx in range(max_v):
		G.addVertex(Vertex(idx, 0, []))

	for idx in range(len(G)):
		degree_per_v = rand.randint(0, max_deg + 1)
		tmp = {idx}
		for i in range(degree_per_v):
			w = choice(tmp, maxvset)
			tmp.add(w)
			G.addEdge(idx, w)
	return G


def randfill(G:GraphByVertex)->bool:
	print(G.all_colors)
	#Start the Process of filling
	for idx, clr in zip(G.G, rand.randint(1, 5, len(G))):
		G.set_colorof(idx.get_idx, clr)

def fill4clr(G:GraphByVertex):
	for idx in range(len(G)):
		used_clr = G.linked_colors(idx) #used_clr is a list
		print(used_clr)
		w = choice(used_clr, (0, 1, 2, 3, 4))
		G.set_colorof(idx, w)

@profile
def main(genV, genDeg):
	G = RandGenAdj(genV, genDeg)
	fill4clr(G)
	Gcount = G.count(by='v')
	print(f"{Gcount=}")
	print(f"{G.all_colors=}")






if __name__ == '__main__':
	#cProfile.run('main(10, 3, colors=colors)')
	for i in rand.randint(10, 35, 20):
		main(i, 3)