# 14시 30분
# 20분 걸림
nh,nm  = map(int,input().split())
term = int(input())

# 시간 덧셈을 위한 준비
hour = term // 60
min = term % 60

# 시간 덧셈
h = nh + hour
m = nm + min


# 덧셈 후 시간 후처리
if m >= 60:
  h =(m // 60)+h
  m = m%60


if h >= 24:
  h = h % 24

print(h,m)