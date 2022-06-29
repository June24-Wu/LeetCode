# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:return None
        newRoot = root
        while newRoot.left != None:
            newRoot = newRoot.left
        def dfs(node):
            if not node:
                return node
            if (node.left == None and node.right == None) or not node:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            left.left = right
            left.right = TreeNode(node.val)
            return left.right
        dfs(root)
        return newRoot
        