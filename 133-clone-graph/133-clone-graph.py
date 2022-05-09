"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:return None
        visited = set()
        table = {} # old : new
        def dfs(node):
            nonlocal visited
            if node in visited:
                return
            table[node] = Node(node.val)
            visited.add(node)
            for i in node.neighbors:
                dfs(i)
            return
        dfs(node)
        visited = set()
        def dfs2(node):
            nonlocal visited
            if node in visited:
                return
            visited.add(node)
            for i in node.neighbors: # old
                table[node].neighbors.append(table[i])
            for i in node.neighbors:
                dfs2(i)
        dfs2(node)
        return table[node]

        # for i in range()
        