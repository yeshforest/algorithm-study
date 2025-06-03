from collections import deque
import sys
input = sys.stdin.readline

# 익은 토마토들의 인접한 곳에 있는 익지않은 토마토는 익게된다
# 며칠이 지나면 익게되는지 최소일수?
# 1은 익은토마토, 0은 익지 않은 토마토, -1은 익지 않은 토마토
# 1인곳에서 bfs수행, 0이면 인접노드로 넘어갈때 +1, -1이면 continue

dx = [-1,1,0,0]
dy = [0,0,1,-1]
queue = deque()


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
queue = deque()

# 모든 익은 토마토의 좌표를 큐에 넣음 (동시 BFS 시작점)
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1  # 날짜 표시
            queue.append((nx, ny))

# 결과 계산
result = 0
for row in graph:
    if 0 in row:
        print(-1)  # 익지 않은 토마토가 있음
        break
    result = max(result, max(row)) # 가장 마지막에 익은 토마토 날짜를 저장

else:
    print(result - 1)  # 처음 1부터 시작했으니 -1
