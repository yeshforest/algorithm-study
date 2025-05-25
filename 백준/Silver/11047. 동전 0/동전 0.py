coin = []
cnt = 0

N, M = map(int, input().split())

for _ in range(N):
  coin.append(int(input()))

coin.sort(reverse=True)

for value in coin:
  cnt = cnt+(M // value)
  M = M % value
  if M <=0 :
    break

print(cnt)