a, b = map(int, input().split())
c = int(input())

total = a*60 + b + c # 전부 분으로 바꿔 계산

h = (total // 60) % 24   # 다시 24시간으로 변환
m = total % 60

print(h, m)