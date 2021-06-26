# README


现在看来，有点危了。


## TODOs
1. 完成四色定理的“验证”
2. **进行地图上色**， 最优方案是作图和ppt里一样的那种，找不到就用结点的那种作图吧
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
## 解释

Vertex,GraphByVertex这两个类主要结构都是列表和字典，但是进行了一点封装。

生成Graph结构我写了3种生成方式：
1. 给定最多节点数MaxVNum, 和每个结点的最多连接点数（度数Degree),然后先初始化一系列空结点。再随机addEdges。但是这样会出现，节点实际上可能会超过那个MaxDegree的限制。（1连了三个点， 但是后来又有两个点连了1，这样1就连了五个点)
2. 是上一种的优化，就是把数量超过的问题解决。
3. 防止0Edge的节点过多。（还在写)

染色方式我没有想到比较高效的
1. 每个节点遍历过去，周围用过的颜色存储到used\_color里面，然后从剩下的部分随机选择颜色。这样是可能导致图形染色无解的，但是速度快。
2. 按颜色来，从Degree最大的点开始，涂色1，然后找到所有可以涂色1的点并染色……进行4次。完成染色(还在写）
3. 有没有别的染色方案？TAT??  




