# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':

        def dfs(node):
            if not node or node in nodes:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if not left:
                return right
            if not right:
                return left
            return node
        return dfs(root)
        