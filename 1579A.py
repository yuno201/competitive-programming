        import random
t=int(input())
n=50
list=["A","B","C"]
s=""
for i in range(t):
    for i in range(random.randrange(1,n)):
        s=s+random.choice(list)
    print(s)
    for i in range(len(s)):
        if "A" in s and "B" in s:
            s.replace("A","") and s.replace("B","")
            if s=="" :
                print('yes')
            elif  "B" in s and "C" in s:
                s.replace("B","")and s.replace("C","")
                if s=="":
                    print('yes')
                else: 
                    print('no')
        s=""

