# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def dfs(node):
            nonlocal ans
            if not node:
                return None
            if not node.left and not node.right:
                ans.append(node.val)
                return None
            node.right = dfs(node.right)
            node.left = dfs(node.left)
            return node
        
        res = []
        
        while root:
            ans = []
            root = dfs(root)
            res.append(ans)
        return res
        