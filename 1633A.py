t=int(input())
for i in range (t):
    n=int(input())
    if n%7==0:
        print(n)
    else:
        x=str(n)
        if len(x)==2:
            if n//10==0:
                while(n%7!=0):
                    n=n+10
            else:
                r=n%7
                n=n-r
                print(n)
        elif len(x)==3:
            if n//100==0:
               while(n%7!=0):
                   n=n+100
            else:
                r=n%7
                n=n-r
                print(n)
                
        
