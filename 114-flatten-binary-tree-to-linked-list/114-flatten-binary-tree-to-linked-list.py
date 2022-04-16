# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(node):
            if not node:return None
            
            dfs(node.left)
            dfs(node.right)
            
            left = node.left
            right = node.right
            node.left = None
            node.right = left
            p = node
            while p.right:
                p = p.right
            p.right = right
        dfs(root)
            
            
        