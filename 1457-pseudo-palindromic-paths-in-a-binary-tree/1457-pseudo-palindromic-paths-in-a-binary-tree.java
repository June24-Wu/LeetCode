# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        ans = 0 ; path = collections.defaultdict(int)
        def dfs(node):
            nonlocal ans ; nonlocal path
            if not node:
                return
            path[node.val] += 1
            if not node.left and not node.right:
                ans += 1 if isValid(path) else 0
                path[node.val] -= 1
                return
            dfs(node.left)
            dfs(node.right)
            path[node.val] -= 1
            return

        def isValid(path):
            cnt = 0
            for i in path:
                if path[i] % 2 != 0:
                    cnt += 1
            return cnt <= 1
        dfs(root)
        return ans