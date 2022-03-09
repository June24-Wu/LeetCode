# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            temp = p
            p = q
            q = temp
        if root == None:return None
        if root.val <= q.val and root.val >= p .val:
            return root
        elif root.val < p.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        return root
        