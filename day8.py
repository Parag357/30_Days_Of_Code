import sys
l1=[]
for i in sys.stdin:
    l1.append(i)
n=int(l1[0])
t1=l1[1:n+1]
d1={}
for i in t1:
    a,b=i.split()
    d1.update({a:b})
t2=l1[n+1:]
for i in t2:
    i=i.strip()
    if i in d1:
        print(i+'='+d1[i])
    else:
        print('Not found')
