# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None ; second = None ; pre = TreeNode(-float("inf"))
        
        def inOrderTraverse(node):
            nonlocal first
            nonlocal second
            nonlocal pre
            if not node :return
            inOrderTraverse(node.left)
            
            if node.val < pre.val:
                if first == None:
                    first = pre
                second = node
            pre = node
            inOrderTraverse(node.right)
        inOrderTraverse(root)
        temp = first.val
        first.val = second.val
        second.val = temp
        
        return