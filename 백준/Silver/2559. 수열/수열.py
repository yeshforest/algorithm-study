# 온도를 측정한 전체 날짜의 수
# 합을 구하기 위한 연속적인 날짜의 수

# 온도의 합이 최대가 되는 값을 출력

# 1 -6 -13 -9 3 10 20 21 5
# 21

n,k = map(int,input().split())
arr = list(map(int,input().split()))

# 누적합 구하기
sums = [0 for _ in range(n+1)] # 1~n까지 사용

for i in range(n): # 0~n
  sums[i+1] = arr[i]+sums[i] # sum[1] = 3 + 0, [0,3,1,-3,-12,-12,-9.-2,11,19,16]

# 최댓값 찾기
answers=[]

for i in range(k,n+1):
  answers.append(sums[i]-sums[i-k]) # 기억 왜곡된걸 그대로 믿음..

print(max(answers))
