st=[]
for s in input():
    if st and st[-1]==s:
        st.pop()
    else:
        st.append(s)
if not st:
    print("yes")
else:
    print("no")
    
            
