"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:return 0
        def dfs(node):
            if node.children == None:
                return 1
            depth = 0
            for i in node.children:
                depth = max(depth,dfs(i))
            return depth + 1
        return dfs(root)
        