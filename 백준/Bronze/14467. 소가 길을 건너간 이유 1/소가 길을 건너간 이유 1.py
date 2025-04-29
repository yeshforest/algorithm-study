n = int(input())
sums = [0] * (n+1)
cows = [-1] * (n+1)
for i in range(1,n+1):
  cow, position = map(int, input().split())
  if cows[cow] != position: # 이전거량 비교했을 때 길을 건넜다면
    cows[cow] = position # 옮기기
    sums[cow] += 1 # 카운트 증가

answers = []
# sums에서 1이랑 0은 제거. 나머지 -1해서 모두 더하기
for i in range(1,n+1):
  value = int(sums[i])
  if value != 1 and value != 0:
    answers.append(value-1)

result=0
for i in range(0,len(answers)):
  result += answers[i]
print(result)