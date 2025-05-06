# n은 홀수
# 1부터 n2까지의 자연수를 달팽이 모양으로..

n = int(input())
target=int(input())
number = n**2

arr = [[0 for _ in range (n)] for _ in range (n)]
x=0
y=0

# 맨 첫 수 저장
arr[x][y] = number
# 초기 아래 -> 오 -> 위 저장
for i in range(n-1): # n-1번 아래로
  x +=1 
  y +=0
  number -= 1
  arr[x][y] = number

for i in range(n-1): # n-1번 옆으로
  x+=0 
  y +=1
  number-=1
  arr[x][y] = number

for i in range(n-1): # n-1번 위쪽으로
  x -=1
  y +=0
  number-=1
  arr[x][y] = number
  

# 왼,아,오,위 반복, 아래 과정을 n-2번 반복
for i in range(n-2):
  if i % 2 == 0: # 짝수번째: 왼, 아 
    for j in range(n-2-i):
      x+=0 
      y-=1 #왼
      number-=1
      arr[x][y] = number
    for j in range(n-2-i):
      x+=1 
      y +=0 #아
      number-=1
      arr[x][y] = number

    
  else: # 홀수 : 오,위
    for j in range(n-2-i):
      x+=0 
      y +=1 #오
      number-=1
      arr[x][y] = number
    for j in range(n-2-i):
      x-=1 
      y-=0 #위
      number-=1
      arr[x][y] = number
    

for i in range(len(arr)):
  for j in range(len(arr)):
    print(arr[i][j],end=" ")
  print("")

for i in range(len(arr)):
  for j in range(len(arr)):
    if arr[i][j] == target:
      print(i+1,j+1)



# 2번
  # n-2번 왼쪽으로
  # n-2번 아래로

# 2번
  # n-3번 위로
  # n-3번 오른쪽으로

# 2번
  # n-4번 왼쪽으로
  # n-4번 아래로


