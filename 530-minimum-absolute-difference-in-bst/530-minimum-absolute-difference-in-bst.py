# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nums = []
        def dfs(node):
            if node == None:return node
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
            return None
        dfs(root)
        print(nums)
        if len(nums) <= 1: return None
        min_val = 10000000000000
        for i in range(1,len(nums)):
            min_val = min(min_val,nums[i] - nums[i-1])
        return min_val
            
            
            
            
        