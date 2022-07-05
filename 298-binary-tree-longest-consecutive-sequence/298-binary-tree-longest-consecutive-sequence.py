# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ans = 1
        def dfs(node): # return (node.val , cnt)
            nonlocal ans
            if not node:
                return (float("inf"),0)
            if not node.left and not node.right:
                return (node.val,1)
            leftVal , leftcnt = dfs(node.left)
            rightVal , rightcnt = dfs(node.right)
            cnt = 1
            if node.val == leftVal - 1:
                cnt = max(cnt,leftcnt + 1)
            if node.val == rightVal - 1:
                cnt = max(cnt,rightcnt + 1)
            ans = max(cnt,ans)
            return (node.val,cnt)
        dfs(root)
        return ans
            