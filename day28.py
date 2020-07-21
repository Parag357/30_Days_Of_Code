n= int(input())
res=[]
for z in range(n):
    l= input().split()
    name = l[0]
    mail = l[1]
    temp=mail.split('@')
    if temp[-1] == 'gmail.com':
        res.append(name)
res=sorted(res)
for i in res:
    print(i)