# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if node == None : return 0
    
            left = dfs(node.left)
            right = dfs(node.right)
            res += abs(left-right)
            return node.val + left + right
        dfs(root)
        return res

        