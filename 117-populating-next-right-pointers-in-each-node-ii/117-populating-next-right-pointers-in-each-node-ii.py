"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:return root
        stack = [root]
        li = []
        size = len(stack)
        cnt = 0
        while stack != []:
            a = stack.pop(0)
            if a.left != None:
                stack.append(a.left)
            if a.right != None:
                stack.append(a.right)        
            li.append(a)
            cnt += 1
            if cnt == size:
                for i in range(len(li)-1):
                    li[i].next = li[i+1]
                li = []
                size = len(stack)
                cnt = 0
        return root
