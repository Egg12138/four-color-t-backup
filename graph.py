#Use no overloading...More effective, More pythonic, but a little inconvienient...
from typing import overload
import numpy as np
class Adjlist:

	def __init__(self, initlist:list):
		self.adj = self.mkdiff(initlist)
		self.edges = sum([len(x) for x in initlist])

	"""
Inut [[2, 3], [3, 5]]=> 
	"""
	def __getitem__(self, idx):
		return self.adj[idx]
	@overload
	def add(self, vs:list, ws:list)->None:
		tmpmax = np.max([col for col in ws])
		if tmpmax >= len(self.adj):
			print(tmpmax)
			self.autogen(self, tmpmax)
		
		for v, w in zip(vs, ws):
			self.adj[v].extend(w)
			for i in w:
				self.adj[i].extend([v])
		self.adj = self.mkdiff(self.adj)
		self.edges = sum([len(x) for x in self.adj])
	@overload
	def add(self, v:int, w:int)->None:
		"""Recommand Way To Add New Nodes And Edge"""

		self.adj[v].append(w)
		self.adj[w].append(v)
		self.edges += 1
	
	def autogen(self, maxlen:int):
		"""
		Extend the array
		"""
		tmp = [[] for i in range(maxlen - len(self.adj) + 1)]
		self.adj.extend(tmp)

	def mkdiff(self, adj:list):
		"""Return an Interable(2D-deep), with every elements different"""
		return [list(set(tmp)) for tmp in adj]

	def shownode(self, idx):
		print("*")
		tmp = self.adj
		for i in tmp[idx]:
			print(f"|---{i}")
		print('\n')





if __name__ == '__main__':

	demo = Adjlist([[2, 4, 5],  [2, 4, 5, 6], [1, 2,4]])
	demo.shownode(1)
	demo.add([0, 1], [[1,2], [2,3,4]])
	demo.shownode(1)