
from networkx.algorithms.assortativity import pairs
from networkx.algorithms.centrality import degree_alg
from algorithm.DataConverter import clear1
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


color_list = ['r', 'lightcyan', 'cyan', 'c', 'teal']#Enumeration...

@profile
def main(maxVnum, maxDegNum, mode='not print'):
	G= RandGenAdj(maxVnum, maxDegNum)
	DeepFirstFillbyIndex(G, 0)
	if mode == '--print' or mode == '-p':
		print('*'*20)
		print(G)
	pairs, fixed_colors = clear1(G)
	Gnx = nx.Graph()
	Gnx.add_edges_from(pairs)
	nx.draw_networkx(Gnx, node_color=fixed_colors)
	plt.show()
if __name__ == '__main__':
	mod = sys.argv[1]
	cProfile.run('main(20, 4, mod)')
	#main(20, 4, sys.argv[1])
