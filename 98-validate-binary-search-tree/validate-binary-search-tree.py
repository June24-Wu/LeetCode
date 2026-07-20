class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node,min_val = -float("inf"),max_val = float("inf")):
            if node == None:
                return True
            if node.val >= max_val or node.val <= min_val:
                return False
            return dfs(node.left,min_val,node.val) and dfs(node.right,node.val,max_val)
        return dfs(root)