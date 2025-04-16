n = int(input())
arr=list(map(int,input().split()))

sums=[0 for _ in range(n+1)]

answes=[]
# 누적합을 구하는데 이득이 되지않는 수를 만나면 이전까지의 값을 다 버린다.
sums[0]=-1001 # 0일때 큰 수가 되지 않게 범위를 벗어나는 작은수 넣음
for i in range(n):
  sums[i+1]=max(sums[i]+arr[i],arr[i])

print(max(sums))