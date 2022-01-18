n=int(input())
x,y=1,1
#입력되는 방향
dir=input().split()
#방향벡터 저장
dx=[0,-1,1,0]
dy=[1,0,0,-1]
move_types=['R','U','D','L']

for d in dir:
 for j in range(len(move_types)):
  if d==move_types[j]:
    nx=x+dx[j]
    ny=y+dy[j]
    
  #범위 넘어가는 경우 무시
  if nx<1 or ny<1 or nx>n or ny>n:
    continue

  #이동 수행
  x,y=nx,ny

print(x,y)
