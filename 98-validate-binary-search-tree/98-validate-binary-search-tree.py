# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node,min_val = -float("inf"),max_val = float("inf")):
            if node == None:
                return True
            if node.val >= max_val or node.val <= min_val:
                return False
            return dfs(node.left,min_val,node.val) and dfs(node.right,node.val,max_val)
        return dfs(root)
            # if node.left == None and node.right == None:
            #     return True
            # elif node.left == None:
            #     return node.val < node.right.val and dfs(node.right)
            # elif node.right == None:
            #     return node.val > node.left.val and dfs(node.left)
            # return node.val < node.right.val and dfs(node.right) and node.val > node.left.val and dfs(node.left)
        # return dfs(root)
            
        