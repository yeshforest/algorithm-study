# 부모 자식 1촌, 할아버지 2촌, 아버지 형제 3촌
from collections import deque
import sys
input = sys.stdin.readline

answer = 0

def bfs(graph,start,visited,target):
  queue = deque()# 시작노드 큐에 넣기
  queue.append([start,0])
  visited[start] = True# 첫번째 노드 방문처리
  cnt=0
  # 방문하지 않은 해당노드와 연결된 모든노드 방문처리
  while queue: # 큐에 아무것도 남지 않을때까지
    current,level = queue.popleft() # 왼쪽에서 하나 뽑아서
    if current == target:
      return level


    for value in graph[current]: # 뽑은 원소와 연결된 원소들을 하나씩 큐에 삽입
      if not visited[value]:
        visited[value] = True # 방문처리
        queue.append([value,level +1])
  return -1
        





n = int(input()) # 전체 사람 수
a,b = map(int,input().split())# 촌수를 계산해야하는 서로다른 두 사람의 번호수
m = int(input()) # 부모 자식들 간의 관계의 개수

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
  x,y = map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)


print(bfs(graph,b,visited,a))