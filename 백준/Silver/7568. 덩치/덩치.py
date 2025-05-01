# 몸무게가 x kg, y cm 덩치는 (x,y)
# 이전의 값들과 비교해서
# 더 작은쪽에 등수를 +1 해주기. 
# 기본 등수는 1
# 정할 수 없으면 그냥두기. 

# 배열필요
n = int(input())
grade = [1]* n

arr = []

for i in range(n):
  x,y = map(int,input().split())
  arr.append([x,y])

for i in range(n):
  for j in range(i+1):
    # i 가 현재 수
    x1=arr[i][0]
    y1=arr[i][1]
    # j가 이전수, 
    x2 = arr[j][0]
    y2 = arr[j][1]
    # 현재수 > 이전수이면 이전수에 +1
    if x1 > x2 and y1 > y2:
      grade[j] +=1
    elif x1< x2 and y1 < y2:
      grade[i] +=1

for i in range(len(grade)):
  print(grade[i], end=" ")

