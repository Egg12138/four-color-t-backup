#Painter!

from Graphy import GraphByVertex, Vertex
from algorithm.Random import choicerest

def nearFilltry(G:GraphByVertex):
	#在速度要求下可以用这种方式生成，但这种可能导致找不到解
	for idx in range(len(G)):
		used_clr = G.linked_colors(idx) #used_clr is a list
		if used_clr is None:
			continue
		#print(used_clr)
		w = choicerest(set(used_clr), {0, 1, 2, 3, 4})
		G.set_colorof(idx, w)



def fill4clr(G:GraphByVertex):
	#能找到优解
	degree_of_vertexes = G.idx_deg_mapping
	pass
