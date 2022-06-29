# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = None ; dis = float("inf")
        
        def dfs(node):
            nonlocal ans ; nonlocal dis
            if not node:
                return
            if abs(node.val - target) < dis:
                dis = abs(node.val - target)
                ans = node.val
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        return ans
        
        