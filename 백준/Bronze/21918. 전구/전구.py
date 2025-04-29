n, order = map(int, input().split())
light = list(map(int, input().split()))


for i in range(order):
  a,b,c = map(int, input().split())
  if a == 1:
    light[b-1] = c
  if a == 2:
    for j in range(b-1,c):
      if light[j] == 0:
        light[j] = 1
      else:
        light[j] = 0
  if a == 3:
    for j in range(b-1,c):
      light[j] = 0
  if a == 4:
    for j in range(b-1,c):
      light[j] = 1


for i in range(len(light)):
  print(light[i], end=" ")