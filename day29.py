t = int(input())
for z in range(t):
    l = input().split()
    n = int(l[0])
    k = int(l[1])
    mx=0
    j=k-1
    for i in range(n,2,-1):
        if i==j:
            continue
        else:
            temp=i&j
            if k>temp>mx:
                mx=temp
    print(mx)
