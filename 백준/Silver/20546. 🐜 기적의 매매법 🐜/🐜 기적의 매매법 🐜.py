money = int(input())
price = list(map(int,input().split()))

jMoney = money # 현금
jStoke = 0 # 주 수
sMoney = money # 현금
sStoke = 0 # 주 수
# 준현: junhun에서 최댓값만큼 삼
# price 끝날때까지 반복해서 결과값내기

for i in range(len(price)):
  buy = 0
  while jMoney - price[i] * (jStoke + 1) >= 0:
    jStoke += 1
    buy = price[i] * jStoke # 가격 * 재고
  jMoney = jMoney - buy

jCurrentMoney = (price[13] * jStoke) + jMoney

# 성민: sMoney에서 
# 3일 연속상승 : 다음 날 전량매도, 3일연속하락 : 다음 날 전량매수

# 3일 전까지 반복
# 마지막날 계산

for i in range(3,len(price)):
  buy = 0
  tempStoke=0
  # 3일연속 하락, 전량매수
  if (price[i-1] - price[i-2] < 0) and (price [i-2] - price[i-3] < 0):
    while sMoney - price[i] * (tempStoke+1) >= 0 : # 돈이 없을때까지
      tempStoke +=1
      buy = price[i] * tempStoke
    sMoney = sMoney - buy
    sStoke += tempStoke
  # 3일연속 상승, 전량매도
  if price[i-1] - price[i-2] > 0 and price [i-2] - price[i-3] > 0:
    if sStoke > 0:
      sMoney += price[i]* sStoke
      sStoke=0

sCurrentMoney = (price[13] * sStoke) + sMoney

if jCurrentMoney == sCurrentMoney:
  print("SAMESAME")
elif jCurrentMoney > sCurrentMoney:
  print("BNP")
elif (jCurrentMoney < sCurrentMoney):
  print("TIMING")

