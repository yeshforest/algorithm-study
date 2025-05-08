n = int(input())
num = int(input())
dx = [-1,0,1,0]
dy = [0,1,0,-1]  # 상, 우, 하, 좌 순서
graph = [[0]*n for _ in range(n)]
number = 2
x = n//2
y = n//2
graph[x][y] = 1 # 배열의 중앙부터 시작
repeat = 1 # 한 방향으로 몇 칸 갈지 결정
i = 0 # dx,dy 가리키는 변수

answer = [x+1,y+1]
while x!=0 or y !=0:
   flag = 0
   for _ in range(2):
      for _ in range(repeat): # 같은 반복 횟수로 두 방향(예: 위-오른쪽)을 이동
         x += dx[i]
         y += dy[i]
         graph[x][y] = number
         if number == num:  # 위치를 찾고자 하는 자연수이면 answer에 위치 저장
            answer = [x+1,y+1] 
         if x == 0 and y == 0: 
            flag = 1 # 좌측 상단(0,0)에 도달했으면 종료 준비
            break 
         number += 1
      if flag == 1: break
      i = (i+1)%4 # 다음 방향으로 전환
   repeat += 1  # 이동 거리 증가

for i in graph:
   print(*i)
   
print(*answer)