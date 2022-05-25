"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:return None
        dummy = Node(0)
        curr = dummy
        def dfs(node):
            nonlocal curr
            if node == None:
                return
            dfs(node.left)
            newNode = Node(node.val)
            curr.right = newNode ; newNode.left = curr ; curr = curr.right
            dfs(node.right)
        dfs(root)
        curr.right = dummy.right; dummy.right.left = curr
        return dummy.right
        
        