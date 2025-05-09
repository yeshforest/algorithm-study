import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    clothes = {}
    
    n = int(input())
    for _ in range(n):
        name, sort = input().split()
        if sort in clothes:  
          clothes[sort].append(name)
        else:
          clothes[sort] = [name]
   
    count = 1
    for key in clothes.keys():
        count *= len(clothes[key]) + 1
    print(count-1)
