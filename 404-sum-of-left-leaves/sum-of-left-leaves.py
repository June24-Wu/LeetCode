# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node,left):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right:
                if left:
                    ans += node.val
                return
            dfs(node.left,True)
            dfs(node.right,False)
            return
        dfs(root,False)
        return ans

        