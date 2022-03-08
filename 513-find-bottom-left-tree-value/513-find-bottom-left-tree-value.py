# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        while stack != []:
            left_val = stack[0].val
            length = len(stack)
            for _ in range(length):
                node = stack.pop(0)
                if node.left != None:
                    stack.append(node.left)
                if node.right != None:
                    stack.append(node.right)
        return left_val
                
                        
        
        