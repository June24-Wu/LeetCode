# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        
        def dfs(node,maxval):
            nonlocal ans
            if not node:
                return
            if node.val >= maxval:
                ans += 1
                maxval = max(node.val,maxval)
            dfs(node.left,maxval)
            dfs(node.right,maxval)
        dfs(root,-float("inf"))
        return ans