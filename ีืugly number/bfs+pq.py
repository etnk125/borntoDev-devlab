from queue import PriorityQueue
x=int(input())
visited={}
ans=[]
queue=PriorityQueue()
def bfs(visited,node,n):
  visited[node]=True
  queue.put(node)
  while queue:
    m=queue.get()
    ans.append(m)
    if m==n:
      return
    for i in [3,11,19]:
      if visited.get(m*i)==None and m*i<=n:
        queue.put(m*i)
        visited[m*i]=True
 
  
bfs(visited,1,3**x)
print(ans[x-1])