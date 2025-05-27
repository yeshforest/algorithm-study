from collections import deque
import sys

input = sys.stdin.readline

def bfs(graph, start, vistied): # bfs의 메서드 정의
  queue=deque([start]) # 시작노드 큐에 넣기
  vistied[start] = True # 시작노드 방문처리
  while queue: # 큐에 아무것도 남지 않을때까지
    v = queue.popleft() # 큐에서 하나의 원소를 뽑음
    #print(v,end=' ') # 큐에서 원소를 하나 뽑아 출력
    
    for i in graph[v]: # 뽑은 원소와 연결된, 아직 방문하지 않은 원소들을 삽입
      if not vistied[i]:
        queue.append(i)
        vistied[i] = True

N,M = map(int,input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)  # 양방향 연결

vistied = [False] * (N+1)

cnt = 0 # 연결 노드의 수
for i in range(1,N+1):
  if not vistied[i]: # 방문하지 않은 노드에서 bfs수행
      bfs(graph,i,vistied)
      cnt += 1 # 수행할 때마다 연결되지 않은것이기 때문에 증가


print(cnt)
