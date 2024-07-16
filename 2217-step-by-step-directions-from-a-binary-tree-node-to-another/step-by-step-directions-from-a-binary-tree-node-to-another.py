# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        parents = {}

        def findDie(node):
            nonlocal parents  ; nonlocal startValue
            if not node:
                return
            if node.val == startValue:
                startValue = node
            if node.left:
                parents[node.left] = node
            if node.right:
                parents[node.right] = node
            findDie(node.left)
            findDie(node.right)
            return
        findDie(root)
        
        queue = [(startValue,"")]
        visited = set()
        while queue:
            node , path = queue.pop(0)
            visited.add(node.val)
            if node.val == destValue:
                return path
            if node in parents and parents[node].val not in visited:
                queue.append((parents[node], path + "U"))
            if node.left and node.left.val not in visited:
                queue.append((node.left,path + "L"))
            if node.right and node.right.val not in visited:
                queue.append((node.right,path + "R"))
        return 

