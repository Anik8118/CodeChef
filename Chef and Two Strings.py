for _ in range(int(input())):
    s1=input()
    s2=input()
    mn=0
    mx=0
    for i in range(len(s1)):
        if s1[i]!='?' and s2[i]!='?':
            if s1[i]!=s2[i]:
                mn+=1 
            elif s1[i]==s2[i]:
                mx+=1 
    print(mn,end=" ")
    print(len(s1)-mx)