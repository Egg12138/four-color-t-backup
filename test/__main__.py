
from networkx.algorithms.assortativity import pairs
from networkx.algorithms.centrality import degree_alg
from algorithm.DataConverter import clear1
from algorithm.Graph_gen import RandGenAdj
from algorithm.Painter import *
from collections import abc
from Graphy import GraphByVertex, Vertex
from numpy import random as rand
from memory_profiler import *
import argparse
import matplotlib.pyplot as plt
import cProfile
import networkx as nx
import numpy as np
import os.path as op
"""
接下来不再需要调试程序，所有就引入一个方便用的ArgParser
"""
#TODO ArgumentParser
#parser = argparse.ArgumentParser(description="Program To Try Four-colors-Theorom")
color_list = ['r', 'lightcyan', 'cyan', 'c', 'teal']#Enumeration...

filep = "/mnt/d/sourcecodes/git/four-colors/test/Demos/"
def ImageSave(file:str, artist, cnt, format='png'):
	if op.isdir:
		filepath = op.join(file, str(cnt), '.png')
	elif op.isfile:
		filepath = file
	artist.savefig(fname=filepath, format=format)


@profile
def main(maxVnum, maxDegNum, mode='not print', cnt=None):
	G= RandGenAdj(maxVnum, maxDegNum)
	DeepFirstFillbyIndex(G, 0)
	if mode == '--print' or mode == '-p':
		print('*'*20)
		print(G)
	
	pairs, fixed_colors = clear1(G)
	Gnx = nx.Graph()
	Gnx.add_edges_from(pairs)
	obj = nx.draw_networkx(Gnx, node_color=fixed_colors)
	plt.savefig(op.join(filep,str(cnt)+'.png'),format='png') 
	plt.clf()
if __name__ == '__main__':
	mod = "--not print"
	#cProfile.runctx('main(20, 4, mod)', None, locals())
	#main(20, 4, sys.argv[1])
	for i in range(20):
		main(20, 5, mod, cnt=i)