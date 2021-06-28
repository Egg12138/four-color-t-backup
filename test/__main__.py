
from networkx.algorithms.assortativity import pairs
from networkx.algorithms.centrality import degree_alg
from algorithm.DataConverter import clear1
from algorithm.Graph_gen import RandGenAdj
from algorithm.Painter import *
from memory_profiler import *
import argparse
import matplotlib.pyplot as plt
import cProfile
import networkx as nx
import os.path as op
"""
接下来不再需要调试程序，所有就引入一个方便用的ArgParser
"""
#TODO ArgumentParser
parser = argparse.ArgumentParser(description="Program To Try Four-colors-Theorom")
parser.add_argument(
	'f',
	type=str,
	action='store',
	help='The dir you wanna figures to be stored'
)
parser.add_argument(
	'-r', '--repeat',
	type=int,
	dest='times',
	default=20,
	help='$times you wanna repeat.Default=20'
)
parser.add_argument(
	'-p',
	dest='willprint',
	action='store_true',
	help='Print the Graph_structure on the standard out(You can use">" to redirect it'
)
parser.add_argument(
	'-s', '--size',
	type=int,
	dest='num_vertexes',
	default=10,
	help='The number of vertexes in the graph, deault=10'
)
parser.add_argument(
	'-d', '--degree', 
	type=int,
	dest='degree',
	action='store',
	default=10,
	help='The max number of degrees per vertexes holds, default=10'
)
args = parser.parse_args()

color_list = ['r', 'lightcyan', 'cyan', 'c', 'teal']#Enumeration...

filep = args.f
times = args.times
willprint = args.willprint
size = args.num_vertexes
max_deg = args.degree
#filep = "/mnt/d/sourcecodes/git/four-colors/test/Demos/"

@profile
def main(maxVnum, maxDegNum, willprint=False, cnt=None):
	if maxDegNum > maxVnum / 2:
		maxDegNum = int(maxVnum) / 2
	G= RandGenAdj(maxVnum, maxDegNum)
	DeepFirstFillbyIndex(G, 0)
	if willprint:
		print('*'*20)
		print(G)
	pairs, fixed_colors = clear1(G)
	Gnx = nx.Graph()
	Gnx.add_edges_from(pairs)
	nx.draw_networkx(Gnx, node_color=fixed_colors)
	plt.savefig(op.join(filep,str(cnt)+'.png'),format='png') 
	plt.clf()

if __name__ == '__main__':
	mod = willprint
	#cProfile.runctx('main(20, 4, mod)', None, locals())
	#main(20, 4, sys.argv[1])
	for i in range(times):
		main(size, max_deg, mod, cnt=i)