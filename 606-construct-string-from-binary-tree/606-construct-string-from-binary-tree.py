# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        res = ""
        
        def dfs(node):
            nonlocal res
            if node == None:return
            if node.left == None and node.right == None:
                res += str(node.val)
                return
            res += str(node.val)
            res += "("
            dfs(node.left)
            res +=")"
            if node.right != None:
                res += "("
                dfs(node.right)
                res +=")"
            return
        dfs(root)
        return res
        