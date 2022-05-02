# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        li = []
        def dfs(node):
            nonlocal li
            if node == None:
                return
            dfs(node.left)
            li.append(node.val)
            dfs(node.right)
        dfs(root)
        # print(li)
        res = float("inf")
        for i in range(1,len(li)):
            res = min(li[i] - li[i-1],res)
        return res
            
        