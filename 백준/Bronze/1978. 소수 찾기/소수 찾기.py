N = int(input())
arr = list(map(int,input().split()))
answer=0

for value in arr: 
  temp = True # 초기값 true
  if value == 1: # 1은 소수 제외
    temp = False
  else:
    for j in range(2,value): #2,3 
      if value != j and value %j ==0 : # 
        temp = False
        break
  if temp:
    answer += 1
  else:
    continue


print(answer)
