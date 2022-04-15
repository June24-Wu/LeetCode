# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        rtVal = - float("inf")
        def dfs(node):
            nonlocal rtVal
            if node == None: return 0
            leftVal = max(0,dfs(node.left)) ; rightVal = max(0,dfs(node.right))
            val = node.val + leftVal + rightVal
            rtVal = max(val,rtVal)
            return node.val + max(leftVal,rightVal)
            
            # return node.val + leftVal + rightVal
        
        dfs(root)
        return rtVal
        