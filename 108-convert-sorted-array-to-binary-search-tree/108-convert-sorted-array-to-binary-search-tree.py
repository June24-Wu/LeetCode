# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # mid_index = len(nums)//2
        # left_index = mid_index - 1
        # right_index = mid_index + 1
        # root = TreeNode(val=nums[mid_index])
        # left = root
        # while left_index >=0:
        #     left.left = TreeNode(nums[left_index])
        #     left_index -= 1
        #     left = left.left
        # right = root
        # while right_index <= len(nums) - 1:
        #     right.right = TreeNode(nums[right_index])
        #     right_index += 1
        #     right = right.right
        # return root
        def f(left,right):
            if left > right:return None
            mid = (left + right)//2
            root = TreeNode(nums[mid])
            root.left = f(left,mid-1)
            root.right  = f(mid+1,right)
            return root
        return f(0,len(nums)-1)
            
        