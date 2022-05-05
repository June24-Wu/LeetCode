# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if node == p or node == q or node == None: return node
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.left == None:
                return node.right
            if node.right == None:
                return node.left
            return node
        return dfs(root)
        