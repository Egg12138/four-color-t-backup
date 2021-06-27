#-*-coding=utf-8-*-
#一个节点索引的异常
class VertexIndexError(Exception):
	def __init__(self, errorline):
		self.error = errorline
