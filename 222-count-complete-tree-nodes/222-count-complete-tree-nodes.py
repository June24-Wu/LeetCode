# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        cnt = 0
        while stack != [] and root != None:
            a = stack.pop(0)
            if a.left != None:
                stack.append(a.left)
            if a.right != None:
                stack.append(a.right)  
            cnt += 1
        return cnt