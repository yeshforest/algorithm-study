# 2원짜리 5원짜리. 동전의 개수가 최소가 되도록 거슬러주자.
money = int(input())

  
# 5원으로 최대 몇개?
# 1개씩 줄여나가며 .. 
answer = 0
two = 0
maxFive = money//5
for i in range(maxFive, -1, -1): # 5원의 개수
  two = (money - (i * 5)) // 2
  # 조건을 만족
  if (i*5 + two*2) == money:
    answer = i+two
    break

if answer == 0:
  print(-1)
else:
  print(answer)