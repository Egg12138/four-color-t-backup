#Painter!

from os import stat
from Graphy import GraphByVertex, Vertex
from algorithm.Random import choicerest

SUCCESSED = True
FAILED = False

color_codes = [1, 2, 3, 4]
def nearFilltry(G:GraphByVertex):
	#在速度要求下可以用这种方式生成，但这种可能导致找不到解(五个颜色)
	for idx in range(len(G)):
		used_clr = G.linked_colors(idx) #used_clr is a list
		if used_clr is None:
			continue
		#print(used_clr)
		w = choicerest(set(used_clr), {0, 1, 2, 3, 4})
		G.set_colorof(idx, w)

def fillVertex(node, spec_clr:int)->bool:
	"""
	node:传入一个节点
	spec_clr:specific color一个被指定的颜色码
	无递归形，对于节点
	"""
	linked_colors = [vertex.get_color for vertex in node.linked_nodes]
	if spec_clr not in linked_colors:
		node.paint(spec_clr)
		return SUCCESSED
	else:
		return FAILED
def fac_fillVertex(node, spec_clr:int)->bool:

	linked_colors = [vertex.get_color for vertex in node.linked_nodes]
	if spec_clr not in linked_colors:
		node.paint(spec_clr)
		for vertex in node.linked_nodes:
			if not vertex.ismarked:
				fac_fillVertex(vertex, spec_clr)
		return fac_fillVertex(node.linked_nodes[0])
	else:
		return FAILED


def DeepFirstFill(G:GraphByVertex, node:Vertex):
	#递归效率低，这里提供非递归方式
	#TODO 非递归染色
	pass

def DeepFirstFillbyIndex(G:GraphByVertex, idx:int)->bool:
	for clr in color_codes:
		status = SUCCESSED
		if clr in [G[v].get_color for v in G.get_edgesof(idx)]:
			status = FAILED
		else:
			G.set_colorof(idx, clr)
		if status and (idx == G.MaxVNum - 1 or DeepFirstFillbyIndex(G, idx+1)):
			return SUCCESSED

	return FAILED