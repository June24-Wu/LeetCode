# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans =  - float("inf")
        
        def dfs(node):
            nonlocal ans
            if node == None:
                return 0
            leftVal = max(0,dfs(node.left)) ; rightVal = max(0,dfs(node.right))
            ans = max(ans,node.val+leftVal+rightVal)
            return node.val + max(leftVal,rightVal)
        dfs(root)
        return ans
        