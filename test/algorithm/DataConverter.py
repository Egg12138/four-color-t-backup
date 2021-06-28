#data_dealer

"""
处理输出。剔除掉零邻接的点。并且返回一个

"""
from networkx.algorithms import link_prediction
import GraphErrors.GraphErrors as GG
from Graphy import GraphByVertex, Vertex


def delta(idx, alist):
    cnt = 0
    for i in alist:
        if idx >= i:
            cnt += 1
    return cnt

def clear0(alist, clrs_list):
    """转换成两两点对， 我们删去没有邻接点的节点
    第一个循环得到一个全部节点非空的列表， 以及那些空列表的index,现在去掉那些index对应的点的颜色"""
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

def clear1(graph:GraphByVertex):
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
        '''
    for vertex in graph.G:
        if not vertex.ismarked:
            newcolors.append(vertex.get_color)
            vertex.set_marked()
            print(f"{newcolors}<--{vertex.get_color}:{vertex.get_idx}")
        for linked_node in vertex.linked_nodes:
            if not linked_node.ismarked:
                newcolors.append(linked_node.get_color)
                print(f"{newcolors}<--{linked_node.get_color}:{vertex.get_idx}")
                linked_node.set_marked()'''
        """   marker = False

    for idx1, clr_idx in zip(result, newcolors):
            print(f"{idx1=}, {graph[idx1[0]].get_color=}, {clr_idx=}")
            if graph.get_color(idx1[0]) == clr_idx:
                marker = True
            else:
                print(graph.get_color(idx1[0]), "----", clr_idx)
                marker = False
                break
        
        if marker and all(newcolors) in clrs_list:"""
    return result, newcolors
   
    print(result)
    print(newcolors)
    