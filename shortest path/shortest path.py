# ppppp
from collections import defaultdict
nnode, nedge = [int(i) for i in input().split()]
dist = defaultdict(lambda: defaultdict(lambda: (float('inf'))))
for i in range(nedge):
    l, r, c = [int(i) for i in input().split()]
    dist[l][r] = dist[r][l] = c
for i in range(nnode):
    dist[i+1][i+1] = 0
for i in range(1, nnode+1):
    for j in range(1, nnode+1):
        for k in range(1, nnode+1):
            dist[j][k] = dist[k][j] = min(dist[j][k], dist[j][i]+dist[i][k])
print(dist[1][nnode])
"""#pp-p-
from queue import Queue
dis={}
visited={}
class Node:
  def __init__(self,data=0):
    self.data=data
    self.neighbor=[]
  def addN(self,node,distance):
    self.neighbor.append([node,distance])
  def getN(self):
    return self.neighbor
  def val(self):
    return self.data
def Dijkstra(node):
  q=Queue()
  q.put(node)
  dis[node]=0
  while not q.empty():
    currentNode=q.get()
    nblist=currentNode.getN()
    for nextNode in nblist:
      if dis.get(nextNode[0])==None:
        dis[nextNode[0]]=nextNode[1]+dis[currentNode]
        q.put(nextNode[0])
      else:
        dis[nextNode[0]]=min( dis[currentNode]+nextNode[1],dis[nextNode[0]])
nnode,nway=[int(i) for i in input().split()]
node=[]
for i in range(nnode):
  node.append(Node(i))
for i in range(nway):
  inp=input().split()
  a=int(inp[0])-1
  b=int(inp[1])-1
  d=int(inp[2])
  node[a].addN(node[b],d)
  node[b].addN(node[a],d)
Dijkstra(node[0])
print(dis[node[-1]])
"""
