from collections import deque

n, m, p = map(int, input().split()) # 노인, TV채널, 처음채널
hate_to_love = {}
visited = [False] * (m+1)
# 채널을 정점으로, 간선을 싫어하는채널 -> 좋아하는 채널로

for _ in range(n):
    love, hate = map(int, input().split())
    if hate not in hate_to_love:
        hate_to_love[hate] = love 
        # hate_to_love = {
            #0 : 1, # 0을 싫어하고 1을 좋아함
            #2:  3, # 2를 싫어하고 3을 좋아함
        # }

queue = deque([p])
visited[p] = True
count = 0

while queue:
    v = queue.popleft() # 하나 꺼내서
    if v not in hate_to_love: # 그 채널이 그래프 안에 없으면 (싫어하는 채널이 없으면?)
        print(count) 
        break
    next_channel = hate_to_love[v]
    if visited[next_channel]: # 이미 방문했으면 사이클
        print(-1)
        break
    visited[next_channel] = True
    queue.append(next_channel) # 다음채널로 바꾸기
    count += 1
