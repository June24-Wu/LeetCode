# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root == None:return 0 
        ans =  - float("inf")
        def dfs(node):
            nonlocal ans
            if node == None:return 0 
            left_cnt = dfs(node.left)
            right_cnt = dfs(node.right)
            node_cnt = 0
            pl = pr = 0
            if node.left != None and node.val == node.left.val:
                pl = left_cnt + 1
            if node.right != None and node.val == node.right.val:
                pr = right_cnt + 1
            ans = max(ans,pl+pr)
            return max(pl,pr)
        dfs(root)
        return ans
            
    
#     def longestUnivaluePath(self, root):
#         self.ans = 0

#         def arrow_length(node):
#             if not node: return 0
#             left_length = arrow_length(node.left)
#             right_length = arrow_length(node.right)
#             left_arrow = right_arrow = 0
#             if node.left and node.left.val == node.val:
#                 left_arrow = left_length + 1
#             if node.right and node.right.val == node.val:
#                 right_arrow = right_length + 1
#             self.ans = max(self.ans, left_arrow + right_arrow)
#             return max(left_arrow, right_arrow)

#         arrow_length(root)
#         return self.ans
        