# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convert(self, root: Optional[TreeNode]):
        if root == None:
            return None
        left = self.convert(root.left)
        right = self.convert(root.right)
        root.left = right
        root.right = left
        return root
    def isSame(self, left: Optional[TreeNode],right: Optional[TreeNode]):
        if left == None and right == None:
            return True
        elif right == None or left == None:
            return False
        elif right.val != left.val:
            return False
        else:
            return self.isSame(left.left,right.left) and self.isSame(left.right,right.right)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = self.convert(root.left)
        right = root.right
        return self.isSame(left,right)
        