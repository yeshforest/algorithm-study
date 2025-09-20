# a ~ b의 바구니를 배열, 반복문 사용해서 역순저장
N,M = map(int,input().split())

array = [x for x in range(N+1)]
temp = array

for i in range(M):
  a,b = map(int, input().split())
  temp = array[a:b+1]
  temp.reverse()
  array[a:b+1] = temp

for i in range(1,N+1):
  print(array[i],end=" ")
