#-*-coding=utf-8-*-
#Graph Class
from collections import abc
from GraphErrors import GraphErrors as GE
from numpy import random as rand
from memory_profiler import *
import numpy as np
import random as rd


class AdjMatrix:
	"""
	使用矩阵来存储
	"""
	def __init__(self):
		self.M = np.array([])# M 是对称方阵
		self.color_store = {}# Mapping...Index to color
	def _out_range(self, idx:int)->bool:
		pass

	def expand(self, to_max:int):
		#TODO expand the matrix.
		pass





#APIs of Vertex:

"""
Demo = Vertex(index=1, value=2, linked=[])
Demo.addLinked(2)
Demo.paint(1)
Demo.get_idx, 
Demo.get_color, 
Demo.get_linked
Demo.ismarked

其中addLinked内包含一个异常类型VertexIndexError,不允许异常Index和自身相连
（多点自环在Graph中来检测）
"""
class Vertex:

	__slots__ = ['_idx', '_color', '_linked_index', '_marked']#Save memory

	def __init__(self, index, value=0, linked=[], marked=False):
		
		self._idx = index#idx'th vertex -> color
		self._color = value#Value can be a symbol, a number or anything
		self._linked_index = linked
		self._marked = marked

	def __repr__(self):

		length = len(self._linked_index)
		string = f"\n*V{self._idx}:    colorcode={self._color}\n"
		if self._linked_index is not None:
			for node in self._linked_index:
				string += f"   |--->{node}\n"
		string += f"   :{length} edge(s)"
		return string 

	def addLinked(self, idx:int)->bool:
		#将Index错误的检测传到Graph里，这里只需要负责添加就行
		if idx >= 0:
			self._linked_index.append(idx)
			return True
		else:
			return False


	def paint(self, colors):
		if colors in [1, 2, 3, 4]:
			self._color = colors
			self._marked = True
			return True
		else:
			return False

	"""
	To avoid change the value of self.attribute uncarefully.
	I creat four functions to get attributes of Vertex
	考虑到可能会不小心访问属性时修改了属性值，引入四个专门的属性访问的函数
	"""

	@property
	def get_idx(self):
		return self._idx 
	@property
	def get_color(self):
		return self._color
	@property
	def get_linked(self):
		return self._linked_index
	@property
	def ismarked(self):
		return self._marked


#APIs of GraphList:

"""
Demo =


"""

class GraphList(list):
	#这个版本继承list，等下看一下接口会不会有问题。

	def __init__(self):
		self.Gl = []

	@property
	def get_linked_indexes(self)->np.ndarray:
		return np.array((vertex.get_linked for vertex in self.G))

	@property
	def get_vertex_by_color(self, key, by='color')->np.ndarray:
		"""按照颜色来访问,如果按index访问，则更应该使用GraphByVertex[index]"""
		if 'color' == by:
			return np.array((v for v in self.G if v.get_color == key ))
		elif 'index' == by:
			self.__getitem__(key)


class GraphByVertex:
	"""另一个版本，不继承list和ndarray, 但是会使用ndarray为部分的数据类型,
	采用无向图
	我们这个类用邻接表， 
	""" 
	def __init__(self):
		self.G = []

	def __repr__(self):
		"""
		建议使用repr(G)来打印，使用print会需要一个返回值 
		建议使用Self[index].value来访问颜色(以及删了额外的接口了)"""
		#return np.array((vertex for vertex in self.G))
		#return np.array_repr(np.array((repr(vertex) for vertex in self.G)))
		for node in self.G:
			print(node)
		return ""
	def __getitem__(self, index):
		return self.G[index]

	def __len__(self):
		"""Number of vertexes"""
		return len(self.G)


	def _auto_gen(self, idx):
		self.G.append([[] for i in range(2 * idx)])

	def _out_range(self, idx):
		return True if len(self.G)-1 < idx else False

	#@profile
	def addVertex(self, node)->bool:
		#允许传入一个
		if isinstance(node, Vertex):
			self.G.append(node)
			return True
		elif isinstance(node, abc.Sequence):
			self.G.append(Vertex(node[0], node[1], []))
			return True
		else:
			return False

	def addVetexes(self, nodes)->bool:
		#TODO 该函数允许接入一个二维数组。。。不过更建议使用Graph生成器来创建Graph
		pass

	#@profile
	def addEdge(self, v, w):
		if v is w or v * w < 0:
			return None
		elif v not in self.G[w].get_linked and w not in self.G[v].get_linked:
			self.G[v].addLinked(w)
			self.G[w].addLinked(v)
		else:
			return None
	'''elif self._out_range(v) or self._out_range(w):
				self._auto_gen(max(v, w))#在先初始化的情况下这个判定可以丢掉了。'''
	
	


	def count(self, by='v'):
		"""size by number of vertexse or size by number of degrees."""
		if by == 'v':
			return len(self.G)
		elif by == 'd':
			return sum([len(vertex.get_linked) for vertex in self.G])
		else:
			raise ValueError(f"{by} is not a valid value for arg by")

	def get_color(self, index):
		return self.G[index].get_color


	def get_edge(self, index):
		return self.G[index].get_linked

	def linked_colors(self, index):
			return {self.G[v_idx].get_color for v_idx in self.G[index].get_linked}

	def self_loop(self, start_index):#
		"""
		深度遍历到最底部，如果得到的index和出发点一样就返回True
		这样算法效率难提高， 应该在图生成的时候就要确保不自环
		"""
		pass

	def set_colorof(self, v_idx, clr_code:int):
		self.G[v_idx].paint(clr_code)





	@property
	def all_edges(self)->np.ndarray:
		return [vertex.get_linked for vertex in self.G]

	@property
	def all_colors(self):
		return [v.get_color for v in self.G]


	@property
	def get_vertex_by_color(self, key, by='color'):
		"""按照颜色来访问点对象
		如果按照index来访问点对象，更应该使用GraphByVertex[index]
		如果按index访问颜色，则更应该使用GraphByVertex.getcolor
		"""
		if 'color' == by:
			return [v for v in self.G if v.get_color == key]
		elif 'index' == by:
			self.__getitem__(key)



"""
class Iterable:
	def __init__(self, vars):
		self.vars = vars

	def __get__(self, instance, cls):
		if instance is None:
			return self
		else:
			return instance.__dict__[self.vars]
"""

def choice(interval, aux_set):
	"""
	interval: Sequence or Set.
	给出一个需要挖掉的点集interval
	以及一个长度为max的母集，返回余下部分的choice
	"""
	if isinstance(interval, abc.Sequence):
		interval = set(interval)
	if isinstance(aux_set, int):
		parent_set = set(list(range(aux_set)))
	elif isinstance(aux_set, abc.Sequence):
		parent_set = set(aux_set)
	else:
		parent_set = aux_set
	rest = parent_set - interval
	#print(f"{rest=}, {parent_set=}, {interval=}")
	return rd.choice(list(rest))

