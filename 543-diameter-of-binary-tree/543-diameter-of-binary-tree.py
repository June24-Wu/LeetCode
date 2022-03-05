# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__():
    #     self.max_val = 0
    def height(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        self.max_val = max(right+left,self.max_val)
        return max(left,right) + 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: 
        self.max_val  = 0
        self.height(root)
        return self.max_val
        