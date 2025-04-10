
n = int(input())
for _ in range(n):
  key=int(input())
  for i in range(2,1_000_001):
    if(key%i ==0): # 몫이고 100만이하의 약수
        print("NO")
        break
    if i == 1_000_000: #100만 이하의 약수가 존재하지 않는다
      print("YES")