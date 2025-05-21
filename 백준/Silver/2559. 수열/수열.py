# 슬라이딩 윈도우로 풀어보자

N,K = map(int,input().split())
days = list(map(int,input().split()))


sum_value = sum(days[:K]) # k전까지의 합
max_value = sum_value # 최댓값의 초기값


# 슬라이딩 윈도우
for i in range(K,N):
  sum_value -= days[i-K] # 왼쪽값은 빼주고
  sum_value += days[i] # 오른쪽 값은 더해줌
  if sum_value > max_value: # 최대값 갱신
      max_value = sum_value


print(max_value)
