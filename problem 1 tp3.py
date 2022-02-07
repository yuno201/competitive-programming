n=int(input())
a=list()
for i in range (1,n):
    if n%i==0:
        for k in range(1000):
            if i==(pow(2,k)-1)*(pow(2,k-1)):
                a.append(i)
x=max(a)
print(x)
