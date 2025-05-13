import math

N = int(input())
arr = list(map(int, input().split()))

min_num = math.gcd(arr[0], math.gcd(arr[1], arr[-1]))

for i in range(1,min_num//2 +1):
  if min_num % i == 0:
    print(i)

print(min_num)
