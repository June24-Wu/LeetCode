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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:return None
        stack = [root]
        return_li = []
        size = len(stack)
        cnt = 0
        
        while stack != []:
            a = stack.pop(0)
            if a.left != None:
                stack.append(a.left)
            if a.right != None:
                stack.append(a.right)   
            return_li.append(a)
            cnt += 1
            if cnt == size:
                for i in range(len(return_li)-1):
                    return_li[i].next = return_li[i+1]
                return_li = []
                size = len(stack)
                cnt = 0
        return root
                