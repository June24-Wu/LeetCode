# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        table = {}
        stack = [root]
        while stack != []:
            node = stack.pop(0)
            if k-node.val in table.keys():
                return True
            table[node.val] = 1
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)
        return False
            
        
        