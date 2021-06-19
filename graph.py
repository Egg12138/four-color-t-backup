from numpy.lib import financial
from adj import Adjlist
import numpy as np
"""
class adj is not the parent if class Graph!!
"""

class Graph:
	#TODO: initialize an adj and apply more 
	pass

	def __init__(self):
		self.adj = Adjlist([])
		#self.vertex_matrix = Matrix([])
		pass

	def __iter__(self):
		return iter(self.adj)

	def __len__(self):
		return len(self.adj)
	"""
	To ensure the security, 
	I sep the add function into addEdge and addVertex
	"""

	def addEdge(self, v:int, w:int):
		if v > len(self.adj) - 1 or w > len(self.adj) - 1:
			raise IndexError("You should call Graph.addVertex to add new vertex ")
		if v is not w:
			self.adj.add(v, w)

	def addVertex(self, v:int, w=None):
		if w is None:
			self.adj.autogen(v)
		else:
			self.adj.add(v, w)

	def shownode(self, idx:int, showzero=True):
		self.adj.shownode(idx, showzero=showzero)





def search(Graph, s:int):
	"""
	Show all vertex linked to the vertex s 
	"""
	try:
		result = Graph.adj[s]
		return result
	except IndexError as ie:
		print("The vertex doesn't exsit.", ie.value)
		return None
	finally:
		print("Done.")




if __name__ == '__main__':
	demo = Graph()
	demo.addVertex(5)
	length = len(demo)
	for i in range(length):
		demo.shownode(i)

	for i in range(length):
		demo.addEdge(i, np.random.randint(i+1))
	print('='*20)

	for i in range(length):
		demo.shownode(i)

	for i in iter(demo):
		print(i)
	#demo.shownode(5, showzero=True)
	
