# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        a = [] ; b = []
        def dfs(node):
            nonlocal a
            if node == None:
                return
            dfs(node.left)
            a.append(node.val)
            dfs(node.right)
        def dfs2(node):
            nonlocal b
            if node == None:
                return
            dfs(node.left)
            b.append(node.val)
            dfs(node.right)
        dfs(root1)
        dfs(root2)
        c = a + b
        c.sort()
        return c
        