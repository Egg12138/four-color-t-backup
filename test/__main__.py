from Graphy import GraphByVertex, Vertex, choice
from numpy import random as rand
import numpy as np


colors = ['red', 'yellow', 'blue', 'green']#Enumeration...

def RandGenAdj(max_v, max_deg=3):

	"""
	max vertex  : max number of vertexes to be generated
	max degree : max number of linked vertex a vertex can have
	"""
	G = GraphByVertex()
	for idx in range(max_v):
		G.addVertex(Vertex(idx, 0, []))

	for idx in range(len(G)):
		degree_per_v = rand.randint(1, max_deg + 1)
		tmp = {idx}
		for i in range(degree_per_v):
			w = choice(tmp, max_v)
			tmp.add(w)
			G.addEdge(idx, w)
	print(G)


if __name__ == '__main__':
	RandGenAdj(10, 3)