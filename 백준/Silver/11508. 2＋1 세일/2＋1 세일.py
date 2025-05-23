# N : 유제품수
# 가격
# 가장 싼것 무료.
# 한번에 3개 사지않으면 정가
N = int(input())
milks = []
for _ in range(N):
  milks.append(int(input()))


money = 0
i = 0

milks.sort(reverse=True)

while i < len(milks):
  if i+2 >= len(milks): # 3개 사지 않는경우
    temp = len(milks)-i # 2
    while temp > 0:
      money += milks[len(milks)-temp]
      temp -=1
  else:
    for j in range(i,i+2): # 3개 사는 경우, 2개만 값 누적
      money += milks[j]
  i += 3 
  
  
print(money)