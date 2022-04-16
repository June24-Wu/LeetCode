# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def isLeaf(node):
            return node.right == None and node.left == None
        
        
        final_list = []
        
        def dfs(node,path):
            nonlocal final_list
            if not node: return
            path.append(str(node.val))
            if isLeaf(node):
                final_list.append(int("".join(path)))
            dfs(node.left,path)
            dfs(node.right,path)
            path.pop()
        dfs(root,[])
        # print(final_list)
        return sum(final_list)
            
        