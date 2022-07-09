"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right == None:
            curr = node
            while curr.parent and curr.parent.val < node.val:
                curr = curr.parent
            if curr.parent and curr.parent.val > node.val:
                return curr.parent
            return None
        curr = node.right
        while curr.left != None:
            curr = curr.left
        return curr
        