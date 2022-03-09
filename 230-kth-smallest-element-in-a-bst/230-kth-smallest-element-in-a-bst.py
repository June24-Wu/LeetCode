# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        li = []
        def dfs(node):
            if node == None:
                return None
            dfs(node.left)
            li.append(node.val)
            dfs(node.right)
            return li
        dfs(root)
        return li[k-1]
            
        