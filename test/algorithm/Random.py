from collections import abc
from numpy import random as rand


def getrestlist(a, b):
	return list(b - a)

def choicerest(used:set, src:set):
	"""
	used: Sequence or Set.
	给出一个需要挖掉的点集used interval
	以及一个母集src，返回余下部分的choice
	Choice From The Rest Of the Src_Set
	used为可变序列或者Set
	src为容器
	"""
	if isinstance(used, abc.MutableSequence) or isinstance(used, abc.MutableSet) and isinstance(src, abc.Container):
		used_set = set(used)
		src_set = set(src)
	else:
		raise TypeError("Wrong Error, Need (MutableSequence/Set, Container")
	rest = getrestlist(used_set, src_set)
	return rand.choice(rest)
	
