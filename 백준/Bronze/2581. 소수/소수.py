# M N (M이상 N이하의 자연수 중 소수인것 골라 소수의 합, 최솟값)
M = int(input())
N = int(input())
arr = []
sum =0
for i in range(M,N+1):
  temp = True
  if i == 1: #1은 소수 제외
    temp = False
  for j in range(2,i):
    if i!=j and i%j ==0:
      temp = False
      break
  if temp:
    arr.append(i)
    sum += i
if len(arr) == 0 and sum ==0:
  print(-1)
else:
  print(sum)
  print(arr[0])