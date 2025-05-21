N, X = map(int,input().split()) # 지난 일 수, x일
visits = list(map(int,input().split())) # 방문자수 리스트

# X일 동안 가장 많이 들어온 방문자 수
# 최대 방문자수 0명 : SAD

# X일동안 구간합이 최대인 갯수

# 최댓값을 기준으로 X일동안 투포인터
if max(visits) == 0:
    print('SAD')
    exit(0)

value = sum(visits[:X]) # x전까지 합
max_value = value # 최댓값의 초기값 
max_cnt = 1

# 슬라이딩 윈도우
for i in range(X,N):# x부터 n-1까지
  value += visits[i] # 다음값 더해주고
  value -= visits[i-X] # 이전값 빼주고

  if value > max_value: # value가 최댓값을 갱신했을 경우
    max_value = value # 최댓값 갱신
    max_cnt = 1 # 초기화
  elif value == max_value:
    max_cnt +=1

print(max_value)
print(max_cnt)

