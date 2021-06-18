#-*-coding=utf-8-*-
#@author:Aydenegg
import numpy as np #Later I will optimize the programm using NP interface.
from typing import overload


class Adjlist:
	
	def __init__(self, initlist:list):
		self.adj =initlist

	def __getitem__(self, idx):
		return self.adj[idx]
	
	def __iter__(self):
		pass

	def add(self, v, w):
		if isinstance()
		self.adj[v].append(w)
		self.adj[w].append(v)


class udGraph:
	"""
	Non-Direction Graph
	number of edge <= (v)(v-1)
	"""
	def __init__(self, numv:int, nume:int):
		if numv * (numv - 1) < nume:
			print("nume too many...")
			self.en = nume
			self.vn = numv
		else:
			self.vn = numv
			self.en = nume
		self.adj = Adjlist([])

	@overload
	def addEdge(self, v:int, w:int)->None:
		"""
		To Add an edge vertex[v] --- vertex[w]
		"""
		self.adj.add(v, w)
		self.en += 1
	@overload
	def addEdge(self, adict:dict)->None:
		for k, v in adict.items():
			self.adj.
	@overload
	def addEdge(self, vls:list, wls:list)->None:
		for vls, wls

	


if __name__ == "__main__":
	demoG = udGraph(10, 20)