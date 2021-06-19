#coding=utf-8
#Author@Aydenegg
#Mail=>xiaojzh7@mail2.sysu.edu.cn

"""
The adj module: Support for the calling and using of Graph-adj.
In a Large sacle of graph, we should seek help from Adj-Matrix.  
*Use no overloading...More effective, More pythonic, but a little inconvienient...
*from typing import overload
"""
#TODO:Optimize the prog using numpy Interface!!!
import collections
import numpy as np
class Adjlist:
	"""Usage:

	*initialization: demo = Adjlist([[1,2], [0], [2])
	*len(demo): Return the lenth of the adj(the number of vertexes).  

	"""
	def __init__(self, initlist:list):
		"""
		There's an unfixed bug. 
		 An empty list in the init functino is recommanded
		"""
		self._adj = self.mkdiff(initlist)
		self.edges = sum([len(x) for x in initlist])
		#print(f"{self.edges=}")
		
	def __getitem__(self, idx):
		return self._adj[idx]
	
	def __len__(self):
		"""
		return the number of vertexes of the adj
		"""
		return len(self._adj)
	def __iter__(self):
		return iter(self._adj)

	def _showit(self, idx):
		print(f"{idx}st*")
		cnt = 0
		for i in range(len(self._adj[idx])):
			print(f"   |---{self._adj[idx][i]}")
			cnt += 1
		print(f'   {cnt}edges\n')
	def addlist(self, vs:list, ws:list)->None:
		"""
		Not Recommanded!
		*addlist(vertex_list, w_list):
		Input a series of vertex_list to be added an edge, and their targets.
		=====
		.g.:
		demo.addlist(vs=[0, 1, 2], ws=[[1], [0,2], [0]])
		then... vertex_0 will be linked with vertex_1
				vertex_1 will be linked with vertex_0 and vertex_2
				vertex_2 will be linked with vertex_0
		"""
		tmpmax = np.max([np.max(col) for col in ws])
		if tmpmax >= len(self._adj):
			self.autogen(tmpmax)
		
		for v, w in zip(vs, ws):
			self._adj[v].extend(w)
			for i in w:
				self._adj[i].extend([v])
		self._adj = self.mkdiff(self._adj)
		self.edges = sum([len(x) for x in self._adj])

	def add(self, vs:int, ws:int)->None:
		"""This is the Recommand Way To Add New Nodes And Edge
		demo.add(1, 2): link the vertex 1 and vertex 2.
		"""
		if self.out_range(vs) or self.out_range(ws):
			self.autogen(max(vs, ws))
		self._adj[vs].append(ws)
		self._adj[ws].append(vs)
		self.edges += 1
	
	def autogen(self, maxlen:int):
		"""
		Extend the array when the index is out of the range.
		"""
		tmp = [[] for i in range(maxlen - len(self._adj) + 1)]
		self._adj.extend(tmp)

	def mkdiff(self, adj:list):
		"""Return an Interable(2D-deep), with all elements different"""
		return [list(set(tmp)) for tmp in adj]

	def out_range(self, idx):
		return (idx > len(self._adj) - 1)

	def shownode(self, idx, showzero=True):
		if self.out_range(idx):
			self.autogen(idx)
		if not showzero:
			if len(self._adj[idx]) != 0:
				print(len(self._adj[idx]))
				self._showit(idx)
		else:
			self._showit(idx)
			





if __name__ == '__main__':

	demo = Adjlist([])
	#demo.addlist([0, 1], [[1,2], [2,3,4]])
	demo.add(1, 5)
	for i in range(len(demo)):
		demo.shownode(i, showzero=False)
	print(f"{demo.edges}edge(s) in total.")
	print(len(demo))