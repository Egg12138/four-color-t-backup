#-*-coding=utf-8-*-

class VertexIndexError(Exception):
	def __init__(self, errorline):
		self.error = errorline
