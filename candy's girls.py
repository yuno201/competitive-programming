t=int(input())
for i in range (t):
    a,b,c,n=map(int,input().split())
    A=(n-2*a+b+c)/3
    B=(n-2*b+a+c)/3
    C=(n-2*c+a+b)/3
    A_int=A.is_integer()
    B_int=B.is_integer()
    C_int=C.is_integer()
    if A_int and B_int and C_int:
        print('yes')
    else:
        print('NO')

