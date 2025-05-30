from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,-2,-2,-1,1,2,2,1]
dy = [2,1,-1,-2,-2,-1,1,2]

def bfs(graph,x,y,targetX,targetY):
    queue = deque([(x,y)]) # 첫번째 노드를 큐에삽입
    # graph[x][y] = 0 # 방문처리
    
    while queue:
      x,y = queue.popleft() # 하나꺼내서 
      # 해당위치에 갈수있는 모든곳으로 가기
 
      for i in range(len(dx)):
        nx = dx[i] + x
        ny = dy[i] + y


        if nx < 0 or ny < 0 or nx >= I or ny >= I:
          continue
        
        if graph[nx][ny] == 0:
          graph[nx][ny] = graph[x][y] + 1 # 방문처리
          queue.append((nx,ny))
    return graph[targetX][targetY]

T = int(input())
for _ in range(T):
  I = int(input()) # 한 변의 길이
  nowX,nowY = map(int,input().split())
  targetX,targetY = map(int,input().split())

  graph = [[0]* I for _ in range(I)]

  if nowX == targetX and nowY == targetY:
    print(0)
  else:
    print(bfs(graph,nowX,nowY,targetX,targetY))
