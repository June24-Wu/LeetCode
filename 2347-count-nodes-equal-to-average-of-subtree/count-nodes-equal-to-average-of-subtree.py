# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return 0 , 0
            left_c, left_sum = dfs(node.left)
            right_c, right_sum = dfs(node.right)

            curr_sum = left_sum + right_sum + node.val
            curr_count = left_c + right_c + 1

            if curr_sum // curr_count == node.val:
                ans += 1
                # print(node.val)
            # print(node.val,curr_count,curr_sum)
            return curr_count, curr_sum
        dfs(root)
        return ans
        