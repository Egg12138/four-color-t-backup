# README


语言不限，
可以跑C或者其他的。
如果算法一开始效率很低， 用CPython会很慢， 所以不一定用Py.

完成玩两个目标后（应该能完成的），要试试改进算法。
## TODOs
1. 完成四色定理的“验证”
2. 进行地图上色
3. 改进算法

## APIs

提供了
Vertex，基本结点
邻接表（用Vertex索引)
两个数据结构。

为了防止调用属性时不小心修改，所以做了一些封装:

Vertex有如下APIs:
* Demo = Vertex(index=1, value=2, linked=[])
* Demo.addLinked(2)添加邻接点
* Demo.paint(1)结点染色
* Demo.get\_idx, 获取节点index
* Demo.get\_color, 获取节点color
* Demo.get\_linked获取节点的临界点indexes列表
* Demo.ismarked标记节点

GraphByVertex有如下的APIs:
G = GraphByVertex()
* G.addVertex(node:Vertex OR Sequence)添加一个节点(可以添加节点对象，或者输入一个节点初始化序列)
* G.addEdge(v:index, w:index)给两个不同的index代表的结点添加一条Edge
* G.count(by='v')统计节点数'v', 总Edges数(Degree)'d'
* G.get\_color(index)获取对应index的节点的颜色
* G.get\_edgesof(index)获取index对应节点的所有邻接点
* G.linked\_colors(index)获取index对应节点的所有邻接点的颜色
* G.set\_colorof(index, color)给index对应的节点上色

提供一个函数
ArrayChoice(used\_set, src\_set)
在未使用过的集合中随机抽取。用在随机连接点，以及相邻点染色的时候。

