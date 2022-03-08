# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        li = []
        def dfs(node:TreeNode):
            if node == None:return None
            if node.left == None and node.left == None:
                li.append(node.val)
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        li = list(set(li))
        li.sort()
        if len(li) > 1:
            return li[1] 
        return -1
        
        