# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        def dfs(node):
            nonlocal path
            if node == None:
                return
            if node.left == None and node.right == None:
                path.append(node.val)
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node
        
        while root != None:
            path = []
            root = dfs(root)
            ans.append(path)
            # print(path)
            # print(ans)
        return ans
            
        