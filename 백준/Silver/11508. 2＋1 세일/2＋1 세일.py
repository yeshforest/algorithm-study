# 전체 합에서 빼주는 경우

n=int(input())
milks = []
for i in range(n):
  milks.append(int(input()))
milks.sort(reverse=True)

money=0
for i in range(2,len(milks),3):
  money+=milks[i]

print(sum(milks)-money)
