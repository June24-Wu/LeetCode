"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:return None
        stack = [root]
        return_li = []
        sub_return = []
        cnt = 0
        size = len(stack)
        
        while stack != []:
            a = stack.pop(0)
            if a.children != None:
                for i in a.children:
                    stack.append(i)
            sub_return.append(a.val)
            cnt +=1
            if cnt == size:
                return_li.append(sub_return)
                sub_return = []
                cnt = 0
                size = len(stack)
        return return_li
            
        