# 입력값 받기
n = int(input())

graph = [0]*1001

xList = []
yList = []

# 왼쪽에서부터 최대높이 전까지 누적합
for a in range(n):
  x,y = map(int,input().split())
  graph[x] = y

  xList.append(x)
  yList.append(y)

maxHeight = max(yList) # 최대높이
maxWidth = max(xList) #최대 x값

preSums= [0]*(maxWidth+2) # !!!!!!!!!!!여기 maxWidth+1해서 틀림.. 배열 인덱스 조심..
nextSums=[0]*(maxWidth+2)

maxHeightX=[]

h=0
# 오른쪽에서부터 최대높이 전까지 누적합
for a in range(1, maxWidth+2):
  if graph[a] == maxHeight: # 최대높이에 도달하면 종료
    maxHeightX.append(a)
    break

  h = max(h,graph[a]) # 이전 h와 현재높이중에 더 높은거로 높이를 정함
  preSums[a] = h + preSums[a-1] # 누적합 구하기


h=0
# 최대높이의 기둥넓이 구하기
for b in range(maxWidth, 0,-1):
  if graph[b] == maxHeight:
    maxHeightX.append(b)
    break
  h = max(h,graph[b])  
  nextSums[b] = h + nextSums[b+1]


# 정답출력
sums = max(preSums) + max(nextSums)

# 최대높이인 구간의 넓이구하기 !!!!!!!!!!!(여기가 구간이 될수있다는걸 생각을 못함)
maxHeightTermWidth = ( maxHeightX[1] - maxHeightX[0] + 1) * maxHeight

answer = sums + maxHeightTermWidth
print(answer)