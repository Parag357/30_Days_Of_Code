t=int(input())
for z in range(t):
    l1=list(input())
    s1="".join(l1[0::2])
    s2="".join(l1[1::2])
    print(s1+" "+s2)