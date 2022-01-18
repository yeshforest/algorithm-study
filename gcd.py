def gcd(x,y):
  if x%y==0:
    return y
  else:
    return gcd(y,x%y)

a,b=map(int,(input().split()))
print(gcd(a,b))