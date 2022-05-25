# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        table = {}
        
        
        queue = [(root,0)]
        while queue != []:
            length = len(queue)
            for _ in range(length):
                node , xLocation = queue.pop(0)
                if xLocation not in table:
                    table[xLocation] = []
                table[xLocation].append(node.val)
                if node.left != None:
                    queue.append((node.left,xLocation-1))
                if node.right != None:
                    queue.append((node.right,xLocation+1))
        key = list(table.keys()) ; key.sort() ; ans = []
        for i in key:
            ans.append(table[i])
        return ans
        