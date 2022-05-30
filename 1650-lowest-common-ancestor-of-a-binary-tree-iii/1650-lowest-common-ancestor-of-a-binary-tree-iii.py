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
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        queue = [p,q]
        visited = set()
        while queue:
            for _ in range(2):
                node = queue.pop(0)
                if node in visited:
                    return node
                visited.add(node)
                if node.parent:
                    queue.append(node.parent)
        return None