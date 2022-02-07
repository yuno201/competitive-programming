import math
n,m=map(int,input().split())
c=0
for a in range (1000):
    for b in range (1000):
        if math.pow(a,2)+b==n and math.pow(b,2)+a==m:
            c=c+1
print(c)
