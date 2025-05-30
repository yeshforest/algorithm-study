from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 0,0으로부터 모든방향으로 검사
def bfs(graph,start,N,M):
  x,y = start
  queue = deque([(x,y)]) # 첫번째 노드 큐에 넣기

  while queue:
    x,y=queue.popleft()
    for i in range(4): 
      nx = dx[i] + x
      ny = dy[i] + y

      if 0<= nx < N and 0 <= ny < M and graph[nx][ny]==1: # 범위 내이고, 방문하지 않았으면
        graph[nx][ny] = graph[x][y] + 1 # 방문처리
        queue.append((nx,ny))
  return graph[N-1][M-1]



# 1 이동 가능, 0 이동불가
N ,M = map(int,input().split()) # 세로로 N칸, 가로로 M칸으로 간주
graph =[]
# visited = [[False]*N for _ in range(M)] # 해당 좌표까지의 최단거리를 저장하면서 방문처리. 1이면 방문 x

for _ in range(N):
  graph.append(list(map(int,input().strip())))



print(bfs(graph,[0,0],N,M))
