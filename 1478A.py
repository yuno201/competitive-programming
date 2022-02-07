from array import*
t=int(input())
arr=()
for i in range (t):
    n=int(input())
    while len(arr)<n:
        arr=list(map(int, input().split()))
    if len(arr)==1:
        s=1
        print(s)
    else:
        s=0
        for x in arr:
            if arr[x]==arr[x+1]:
                s=s+1
        arr *= 0
    print(s)
   
