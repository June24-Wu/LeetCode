# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        step = 0
        def dfs(node):
            nonlocal step
            if node == None:return 0
            left = dfs(node.left)
            right = dfs(node.right)
            step += abs(left) + abs(right)
            return node.val + left + right - 1
        dfs(root)
        return step
        