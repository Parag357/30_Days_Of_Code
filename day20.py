import sys
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
c=0;
for i in range(n):
    for j in range(n-1-i):
        if a[j]>a[j+1]:
            temp=int(a[j])
            a[j]=a[j+1]
            a[j+1]=temp;
            c+=1
print('Array is sorted in %d swaps.' %(c))
print('First Element: %d' %(a[0]))
print('Last Element: %d' %a[-1])