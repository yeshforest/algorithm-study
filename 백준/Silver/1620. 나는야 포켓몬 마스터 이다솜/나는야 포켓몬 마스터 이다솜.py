# 포캣몬 개수n
# 내가 맞춰야 하는 문제의 개수 M
# N 첫글자 대문자. 일부는 마지막만 대문자.
# 최대 이름 20. 최소 2
# 알파벳 -> 포켓몬 번호 
# 포켓몬 번호 -> 문자출력 (1<= 번호 <=N)
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dict = {}


for i in range(1,N+1):
  name = input().strip()
  dict[i] = name
  dict[name] = i

for i in range(M):
  problem = input().strip()
  if problem.isdigit():
    print(dict[int(problem)])
  else:
    print(dict[problem])


# 위 방식은 시간초과. O(N+M*N)