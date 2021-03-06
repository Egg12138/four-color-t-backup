registry = {}
"""一个重载的装饰器，不用了……"""

class MultiMethod:
	def __init__(self, name):
		self.name = name
		self.typemap = {}
	def __call__(self, *args):
		types = tuple(arg.__class__ for arg in args)
		functinon = self.typemap.get(types)
		if functinon is None:
			raise TypeError("No Match")
		return function(*args)
	
	def register(self, types, function):
		if types in self.typemap:
			raise TypeError("duplcate registration")
		self.typemap[types] = function


def multimethod(*types):
	def register(function):
		name = function.__name__
		mm = registry.get(name)
		if mm is None:
			mm = registry[name] = MultiMethod(name)
		mm.register(types, function)
	return register
