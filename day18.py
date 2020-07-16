import sys

class Solution:
    # Write your code here
    top=-1
    front=-1
    rear=-1
    l1=[]
    l2=[]
    def pushCharacter(self,item):
        self.top+=1
        self.l1.append(item)
    def enqueueCharacter(self,item):
        if self.front==-1:
            self.front=0
        self.rear+=1
        self.l2.append(item)
    def popCharacter(self):
        if self.top==-1:
            return None
        self.top-=1
        return self.l2.pop()
    def dequeueCharacter(self):
        if self.front==-1:
            return None
        else:
            res=self.l2[0]
            self.l2=self.l2[1:]
            return res


# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    