import numpy as np


def choicerest(used:set, src:set):
	if isinstance(used, abc.MutableSequence) or isinstance(used, abc.MutableSet) and isinstance(src, abc.Container):
		used_set = set(used)
		src_set = set(src)
	else:
		raise TypeError("Wrong Error, Need (MutableSequence/Set, Container")
	rest = getrestlist(used_set, src_set)
	return rand.choice(rest)
	
