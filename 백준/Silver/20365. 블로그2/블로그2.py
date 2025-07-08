# n 칠해야 하는 문제의 수
# R은 빨간색, B는 파란색

# 덩어리 수가 더 적은거에 +1

N = int(input())
problems = list(input())

blue = 0
red = 0

prev = ''

for p in problems:
  if p != prev:
    if p == 'R':
      red +=1
    elif p == 'B':
      blue +=1
  prev = p


print(min(blue,red) +1)