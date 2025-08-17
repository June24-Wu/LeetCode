class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        result = 0
        def dfs(node,parent):
            nonlocal result 
            if node is None:
                return (0,0)
            left = dfs(node.left,node)
            right = dfs(node.right,node)
            if parent.left==node:
                result = max(result,right[0]+1)
            else:
                result = max(result,left[1]+1)
            return (left[1]+1,right[0]+1)
        dfs(root.left,root)
        dfs(root.right,root)
        return result