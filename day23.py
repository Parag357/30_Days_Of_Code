import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def levelOrder(self,root):
        l=[]
        l.append(root)
        while len(l)!=0:
            temp=l[0]
            print(temp.data,end=' ')
            l=l[1:]
            if temp.left !=None:
                l.append(temp.left)
            if temp.right !=None:
                l.append(temp.right)

        #Write your code here

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
