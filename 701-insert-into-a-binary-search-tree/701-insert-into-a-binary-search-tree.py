# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:return TreeNode(val)
        node = root
        while node != None:
            if node.val > val:
                if node.left == None:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
            else:
                if node.right == None:
                    node.right = TreeNode(val)
                    break
                node = node.right
        return root
        