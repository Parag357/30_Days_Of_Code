a=input().split(' ')
e=input().split(' ')
for i in range(3):
    a[i]=int(a[i])
    e[i]=int(e[i])
fine=0
if a[2]>e[2]:
    fine=10000
elif a[2]==e[2]:
    if a[1]>e[1]:
        fine=(a[1]-e[1])*500
    elif a[1]==e[1]:
        if a[0]>e[0]:
            fine=(a[0]-e[0])*15
print(fine)
