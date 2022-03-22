# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(array):
            if array == []:return None
            mid_index = array.index(max(array))
            root = TreeNode(array[mid_index])
            root.left = dfs(array[:mid_index])
            root.right = dfs(array[mid_index+1:])
            return root
        return dfs(nums)
            
        