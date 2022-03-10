# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        table = {}
        def dfs(node):
            if node == None:return None
            dfs(node.left)
            if node.val not in table.keys():
                table[node.val] = 1
            else:
                table[node.val] +=1
            dfs(node.right)
            return
        dfs(root)
        
        max_count = 0
        for i in table.keys():
            if table[i] > max_count:
                val = [i]
                max_count = table[i]
            elif table[i] == max_count:val.append(i)
        return val
        