# 준현이 VS 성민이

Money = int(input())                                # 초기 현금
MachineDuck = list(map(int, input().split()))       # 1일부터 14일까지의 주가

# 준현이
jMoney = Money    # 현금 
jStoke = 0 # 주 수

# 성민이
sMoney = Money
sStoke = 0

for idx, price in enumerate(MachineDuck): # 인덱스와 값을 동시에 접근

    # 준현
    jStoke += (jMoney // price)
    jMoney %= price

    # 성민
    temp = MachineDuck[idx:idx+4] # 현재 index ~ index+3

    if len(temp) < 4: # 3개 이하이면 범위 벗어나므로 넘어가기
        continue

    if temp[0] < temp[1] < temp[2] < temp[3] and sStoke > 0:         # 매도
        sMoney += (sStoke * temp[3])
        sStoke = 0
    elif temp[0] > temp[1] > temp[2] > temp[3]:                             # 매수
        sStoke += (sMoney // temp[3])
        sMoney %= temp[3]

answer_bnp = jMoney + jStoke * MachineDuck[-1] # 맨뒤의 값..
answer_timing = sMoney + sStoke * MachineDuck[-1] 

if answer_bnp < answer_timing:
    print("TIMING")
elif answer_bnp > answer_timing:
    print("BNP")
else:
    print("SAMESAME")