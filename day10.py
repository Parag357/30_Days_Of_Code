import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input())
    n1=n
    s=''
    while(n1>0):
        s=str(n1%2)+s
        n1//=2
    cnt=int(0)
    max=int(0)
    for i in s:
        if i=='1':
            cnt+=1
            if cnt>max:
                max=cnt
        else:
            cnt=0
    print(max)
