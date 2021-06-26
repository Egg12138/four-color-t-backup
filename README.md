# README


语言不限，
可以跑C或者其他的。
如果算法一开始效率很低， 用CPython会很慢， 所以不一定用Py.

完成玩两个目标后（应该能完成的），要试试改进算法。
## TODOs
1. 完成四色定理的“验证”
2. 进行地图上色
3. 改进算法
<<<<<<< HEAD

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

=======
4. C接口

## Logs

2021-06-15:
Initialization.

2021-06-16->06-18
摸鱼

2021-06-19:
完成了无向图的基本内容。
（不过我做完才发现我搞错了。。。我们的图的需求应该是一个树并且每个数都有值，，，）
把邻接表封装了一层（其实没什么必要， 写完adj类才反应过来，但是不如就直接写掉了）

2021-06-22:
下周要完成作业，所以今天开始重新写了数据结构。
在test目录下，已经有整个项目的基本结构了
然后把用邻接表作的图的内部方法优化了一下
接口部分基本完成（可能会加入多维数组的传入来生成图）

准备写深度优先的遍历。
2021-06-23:
我似乎忘了一点限制条件。。。就是不能有奇怪的交错。。。
今晚再改
>>>>>>> 9c0a359261fc64b2b9fcaee6d9be884f009eb269
