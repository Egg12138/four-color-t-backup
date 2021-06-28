#-*-coding=utf-8-*-
#data_dealer


import GraphErrors.GraphErrors as GG
from Graphy import GraphByVertex


def delta(idx, alist):
    cnt = 0
    for i in alist:
        if idx >= i:
            cnt += 1
    return cnt

def clear0(alist, clrs_list):
    """常规转化"""
    result = []
    toberm = []

    for index, linked in enumerate(alist):
        if len(linked) != 0:
            print(f"{index=}, {linked=}")
            for linked_index in linked:
                result.append((index, linked_index))
        else:
            toberm.append(index)
    
    newcolors = [clr for idx,clr in enumerate(clrs_list) if idx not in toberm]
    return result, newcolors

def clear1(graph:GraphByVertex)->tuple:
    """
    Return result, newcolors
    首先去除掉可能存在的0邻接点（虽然现在的生成函数是不会生成0邻接点）
    然后转化成能够被networkx.Graph接收的形式：result= ((0, 1), (0, 2)...(10, 6))
    然后对颜色列表的顺序进行转化
    因为networkx是按照0-->1, 2, 3; 1-->0, 3, 5; 2-->0, 6; 3-->0, 4 ==> 0, 1, 2, 3, 5, 6...
    的这个顺序染色的
    
    """
    result = []
    toberm = []
    newcolors = []
    for vertex in graph.G:
        vertex.set_unmarked()
        if len(vertex.get_linked) != 0:
            for linked_index in vertex.get_linked:
                result.append((vertex.get_idx, linked_index))
        else:
            toberm.append(vertex.get_idx)

    for edge_tuple in result:
        """Less Efficiency"""
        main_index = edge_tuple[0]
        later_index = edge_tuple[1]
        if not graph[main_index].ismarked:
            newcolors.append(graph[main_index].get_color)
            graph[main_index].set_marked()
        if not graph[later_index].ismarked:
            newcolors.append(graph[later_index].get_color)
            graph[later_index].set_marked()
    #check:
    if not all(newcolors) in graph.all_colors:
        print(f"{newcolors=}\n\n{graph.all_colors=}")
        raise GG.UnPairedError("Colors Unpaired!")
    return result, newcolors

    