# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        isLeafNode = lambda root: not root.left and not root.right
        
        def dfs(node):
            val = 0
            if node.left:
                val += node.left.val if isLeafNode(node.left) else dfs(node.left)
            if node.right and not isLeafNode(node.right):
                val += dfs(node.right)
            return val
        return dfs(root) if root else 0
                
        