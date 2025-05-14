# B진법 수 N을 10진법으로 출력한다
N,B = input().split()
N = N[::-1]
B=int(B)

result = 0

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(N)):
  result += (int(B)**i)*(number.index(N[i]))

print(result)

