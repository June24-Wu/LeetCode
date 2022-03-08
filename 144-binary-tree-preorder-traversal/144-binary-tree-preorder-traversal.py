# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li = []
        def dfs(node):
            if node == None:
                return None
            li.append(node.val)
            dfs(node.left)
            dfs(node.right)
            return None
        dfs(root)
        return li
        