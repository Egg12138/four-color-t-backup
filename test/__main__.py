
from networkx.algorithms.centrality import degree_alg
from algorithm.DataConverter import clear0
from algorithm.Graph_gen import RandGenAdj
from algorithm.Painter import *
from collections import abc
from Graphy import GraphByVertex, Vertex
from numpy import random as rand
from memory_profiler import *

import matplotlib.pyplot as plt
import cProfile
import networkx as nx
import numpy as np
import sys

"""
现在已经有了一个随机生成连接情况的图
下一步是上色。
最后可视化就再说了吧。

"""


color_list = ['gray', 'red', 'yellow', 'blue', 'green']#Enumeration...

#@profile
def main(maxVnum, maxDegNum, mode='not print'):

	#Generate Graph
	G = RandGenAdj(maxVnum, maxDegNum)
	#Paint the Graph
	nearFilltry(G)
	Gcount = G.count(by='v')
	print(f"{Gcount=}")
	print(f"{G.all_edges=}|||{G.all_colors=}")
	if mode == 'print':
		print(G)
	#Draw
	dealt_pairs, dealt_colors = clear0(G.all_edges, G.all_colors)
	Gnx = nx.Graph()
	Gnx.add_edges_from(dealt_pairs)#传入无向图库
	#colors = [color_list[clr_code] for clr_code in dealt_colors]
	nx.draw_networkx(Gnx, node_color=dealt_colors)
	plt.show()




if __name__ == '__main__':
	#cProfile.runctx('main(20, 3)', None, locals())
	main(10, 3, sys.argv[1])
