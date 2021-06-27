#data_dealer

"""
处理输出。剔除掉零邻接的点。并且返回一个

"""
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
            for linked_index in linked:
                delta1 = delta(index, toberm)
                delta2 = delta(linked_index, toberm)
                result.append((index - delta1, linked_index - delta2))
        else:
            toberm.append(index)
    
    newcolors = [clr for idx,clr in enumerate(clrs_list) if idx not in toberm]
    return result, newcolors