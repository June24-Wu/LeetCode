# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        stack = [root]
        result = []
        while stack != []:
            total = 0
            length = len(stack)
            for _ in range(length):
                node = stack.pop(0)
                total += node.val
                if node.left != None:
                    stack.append(node.left)
                if node.right != None:
                    stack.append(node.right)
            result.append(total/length)
        return result
            
            
                
            
            
        