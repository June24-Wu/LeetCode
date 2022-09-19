# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        table = collections.defaultdict(set)
        
        def dfs(node,depth):
            if not node:
                return None
            table[depth].add(node.val)
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
            return
        dfs(root,0)
        max_depth = max(list(table.keys()))
        nodes = table[max_depth]
        
        def ans(node):
            if not node or node.val in nodes:
                return node
            left = ans(node.left)
            right = ans(node.right)
            if left and right:
                return node
            if left:
                return left
            return right
        return ans(root)
        