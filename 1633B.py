t=int(input())
a=''
b=''
r=0
for i in range(t):
    s=str(input())
    if len(s)==1:
        print('1')
    else:
        for i in range(len(s)):
            if s[i]=='0':
                a=a+'0'
            else:
                b=b+'1'
        if len(a)<len(b):
            for i in range(len(s)):
                if s[i]=='0':
                    r=r+1
            print(r)
        elif len(a)>len(b):
            for i in range(len(s)):
                if s[i]=='1':
                    r=r+1
            print(r)
        else:
            print(r)
        r=0
            
        
        
        
