# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, left: Optional[TreeNode],right: Optional[TreeNode]):
        if left == None and right == None:
            return True
        elif right == None or left == None:
            return False
        elif right.val != left.val:
            return False
        else:
            return self.isSame(left.left,right.left) and self.isSame(left.right,right.right)
            
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # return self.isSame(root.left,subRoot)
        stack = []
        if root == None:
            return False
        stack.append(root)
        while stack != []:
            node = stack.pop(0)
            if (node.val == subRoot.val):
                if self.isSame(node,subRoot):
                    return True
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)
        return False
            
        