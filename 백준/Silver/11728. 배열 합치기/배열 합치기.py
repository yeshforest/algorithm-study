N, M = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

new = a+b

new.sort()

for i in new:
  print(i,end=" ")
