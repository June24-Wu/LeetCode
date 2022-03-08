# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li = []
        def dfs(node):
            if node == None: return None
            dfs(node.left)
            dfs(node.right)
            li.append(node.val)
            return None
        dfs(root)
        return li
        