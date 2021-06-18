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

	def __init__(self, initlist:list):
		self._adj = self.mkdiff(initlist)
		self.edges = sum([len(x) for x in initlist])

		"""
	Inut [[2, 3], [3, 5]]=> 
		"""
	def __getitem__(self, idx):
		return self._adj[idx]
	
	def __len__(self):
		"""
		return the number of vertexes of the adj
		"""
		return len(self._adj)

	def addlist(self, vs:list, ws:list)->None:
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
		"""Recommand Way To Add New Nodes And Edge"""
		if vs > len(self._adj) - 1 or ws > len(self._adj) - 1:
			self.autogen(max(vs, ws))
		self._adj[vs].append(ws)
		self._adj[ws].append(vs)
		self.edges += 1
	
	def autogen(self, maxlen:int):
		"""
		Extend the array
		"""
		tmp = [[] for i in range(maxlen - len(self._adj) + 1)]
		self._adj.extend(tmp)

	def mkdiff(self, adj:list):
		"""Return an Interable(2D-deep), with every elements different"""
		return [list(set(tmp)) for tmp in adj]

	def shownode(self, idx):
		print(f"{idx+1}st*")
		for i in range(len(self._adj[idx])):
			print(f"   |---{self._adj[idx][i]}")
		print(f'   {i+1}edges\n')





if __name__ == '__main__':

	demo = Adjlist([[2, 4, 5],  [2, 4, 5, 6], [1, 2,4]])
	demo.addlist([0, 1], [[1,2], [2,3,4]])
	demo.add(1, 5)
	for i in range(len(demo)):
		demo.shownode(i)
	print(f"{demo.edges}edge(s)")