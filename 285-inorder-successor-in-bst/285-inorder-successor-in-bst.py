# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        ans = []
        
        def dfs(node):
            nonlocal ans
            if node == None:
                return
            dfs(node.left)
            ans.append(node)
            dfs(node.right)
        dfs(root)
        for i in range(1,len(ans)):
            if ans[i-1].val == p.val:
                return ans[i]
        return None
            
        