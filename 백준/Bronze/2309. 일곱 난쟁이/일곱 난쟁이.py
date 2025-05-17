# 9난쟁이 중 7명의 난쟁이의 키를 더해서 100이 되는 경우를 오름차순으로 출력

heights = []
answer= 0

for _ in range(9):
  height = int(input())
  heights.append(height)

#print(heights)

  

for i in range(9):
  finish = False
  for j in range(1,9):
    if i != j:
      a = heights[i]
      b = heights[j]
      if (sum(heights) -a -b) == 100:
        heights.remove(a)
        heights.remove(b)
        
        finish =  True
        break
  if finish:
    break

heights.sort()
for i in heights:
  print(i)

