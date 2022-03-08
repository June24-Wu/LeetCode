# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def private(self, root: Optional[TreeNode], targetSum: int):
        if root == None:
            return 0
        count = 0
        if targetSum == root.val:
            count += 1
        count = count + self.private(root.left,targetSum-root.val) + self.private(root.right,targetSum-root.val)
        return count
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root == None:
            return 0 
        return self.private(root,targetSum) + self.pathSum(root.left,targetSum) + self.pathSum(root.right,targetSum)
        