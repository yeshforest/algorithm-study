# 1 ~ N 번공
# 0 ~ N+1까지의 배열 -> 1 ~ N까지 배열 사용

N, M = map(int,input().split())
array = [x for x in range(N+1)] # 1 ~ N

for i in range(M):
  a,b = map(int,input().split())
  temp = array[a]
  array[a] = array[b]
  array[b] = temp

for i in range(1,N+1):
  print(array[i],end=" ")