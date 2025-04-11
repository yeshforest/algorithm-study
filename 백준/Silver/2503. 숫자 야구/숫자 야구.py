n = int(input())
# 자리까지 맞으면 스트라이크
# 숫자만 맞으면 볼
# bf는 문제를 푸는사람입장에서 마구잡이로 시도하는것인데, 문제를 내는사람 입장에서 생각했다. 

hint = [list(map(int,input().split())) for _ in range(n)]
answer=0
# [[123,1,1], [346,1,0]...]

for a in range(1,10): # 이렇게 100의 자리수를 모두 시도해보기
  for b in range(1,10): 
    for c in range(1,10):
      if a == b or b == c or c == a: # 같은 수는 있을 수 없기때문에 넘어가기
        continue
      cnt = 0

      # 숫자가 정해졌다면
      for arr in hint: #[123,1,1]
        number = str(arr[0])
        strike = arr[1]
        ball = arr[2]

        # a,b,c와 number를 비교, 직접 answer올리기
        # 스트라이크
        str_cnt = 0
        if a == int(number[0]): # 자리까지 맞으면
          str_cnt = str_cnt +1
        if b == int(number[1]):
          str_cnt = str_cnt + 1
        if c == int(number[2]): 
          str_cnt = str_cnt + 1

        # 볼 
        ball_cnt = 0 
        if a == int(number[1]) or a == int(number[2]):
          ball_cnt = ball_cnt+1
        if b == int(number[0]) or b == int(number[2]):
          ball_cnt = ball_cnt+1
        if c == int(number[0]) or c == int(number[1]):
          ball_cnt = ball_cnt+1
        
        if ball == ball_cnt and strike == str_cnt: # 시도하다가 이런 조건에 맞으면
          cnt = cnt+ 1


      if cnt == n: # cnt = 조건에 맞는 횟수 증가
        answer= answer+1 
print(answer)
