# 통로의 세로길이 N 가로길이 M 음쓰 개수 K
# 좌표 r,c
from collections import deque
import sys

input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 모든 위치에서 bfs수행
# 연결된 최대갯수 출력
def bfs(graph,x,y,N,M):
  queue = deque([(x,y)]) #큐에 시작노드 삽입
  graph[x][y] = 0 # 방문처리
  cnt = 1

  while queue:
    x,y = queue.popleft() # 큐에서 하나 꺼내서
    for i in range(4): # 연결된 상하좌우 중에
      nx = x + dx[i]
      ny = y + dy[i]
      if nx <= 0 or ny <= 0:
        continue
      if nx > N or ny > M:
        continue
      if graph[nx][ny] == 1: # 쓰레기가 있으면
        graph[nx][ny] = 0
        queue.append((nx,ny))
        cnt+=1
  return cnt

N,M,K = map(int,input().split())
graph = [[0] *(N+1) for _ in range(M+1)]
max_size = 0
for _ in range(K):
  a,b = map(int,input().split())
  graph[b][a] = 1
# print(graph)

for i in range(1,N+1): # y, 
  for j in range(1,M+1): # x
    if graph[j][i] == 1: # 쓰레기가 있으면
      max_size = max(max_size,bfs(graph,j,i,M,N)) # bfs수행
print(max_size)