# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ans = 1
        def dfs(node): # return (node.val , max increse , max decrease)
            nonlocal ans
            if not node:
                return (float("inf"),0,0)
            if not node.left and not node.right:
                return (node.val,1,1)
            leftval , leftin , leftde = dfs(node.left)
            rightval , rightin , rightde  = dfs(node.right)
            inc , de = 1 , 1
            if node.val - rightval == 1:
                de = max(de,rightde + 1)
            if node.val - leftval == 1:
                de = max(de,leftde + 1)
            if node.val - rightval ==  - 1:
                inc = max(inc,rightin + 1)
            if node.val - leftval == - 1:
                inc = max(inc,leftin + 1)
            ans = max(ans,inc + de - 1)
            return (node.val,inc,de)
        dfs(root)
        return ans
        