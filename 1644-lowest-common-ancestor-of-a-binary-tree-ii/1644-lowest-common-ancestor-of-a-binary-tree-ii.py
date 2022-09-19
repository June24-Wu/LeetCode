# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        table = set()
        
        def dfs(node):
            if not node:
                return node
            table.add(node.val)
            left = dfs(node.left)
            right = dfs(node.right)
            if node.val == p.val or node.val == q.val:
                return node
            if not left:
                return right
            if not right:
                return left
            return node
        ans = dfs(root)
        if p.val not in table or q.val not in table:
            return None
        return ans
        