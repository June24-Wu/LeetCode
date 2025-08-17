# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(node):
            if not node:
                return [], 0

            left_vals, left_cnt = dfs(node.left)
            right_vals, right_cnt = dfs(node.right)

            left_vals = [i + node.val for i in left_vals]
            right_vals = [i + node.val for i in right_vals]

            vals = left_vals + right_vals + [node.val]
            ans = 0
            for i in vals:
                if i == targetSum:
                    ans += 1
            # print(node.val,vals,ans)
            return vals, ans + left_cnt + right_cnt
        return dfs(root)[1]

        