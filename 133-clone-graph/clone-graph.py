"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        vis = {}
        def dfs(node):
            nonlocal vis
            if node.val in vis:
                return vis[node.val]
            new_node = Node(node.val)
            vis[node.val] = new_node
            for neighbor in node.neighbors:
                new_neighbor = dfs(neighbor)
                # new_neighbor.neighbors.append(new_node)
                new_node.neighbors.append(new_neighbor)
            return new_node
        return dfs(node)

        