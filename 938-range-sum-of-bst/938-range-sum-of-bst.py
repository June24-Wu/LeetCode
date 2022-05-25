# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        ans = 0
        def dfs(node,left,right):
            if left > high or right < low or node == None:
                return
            nonlocal ans
            if low <= node.val <= high:
                ans += node.val
            dfs(node.left,left,node.val)
            dfs(node.right,node.val,right)
        dfs(root,-float("inf"),float("inf"))
        return ans
            
        