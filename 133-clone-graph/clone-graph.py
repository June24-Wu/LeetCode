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
        vis = {}
        def dfs(node):
            if node in vis:
                return vis.get(node)
            if not node:
                return None
            clone_node = Node(node.val)
            vis[node] = clone_node
            for adj in node.neighbors:
                # print(node.val,adj.val)
                clone_node.neighbors.append(dfs(adj))
            return clone_node

        return dfs(node)
            


        