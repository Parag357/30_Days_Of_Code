t=int(input())
for z in range(t):
    n=int(input())
    cnt=0
    if n==1:
        print('Not prime')
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                cnt+=1
        if cnt>0:
            print('Not prime')
        else:
            print('Prime')
