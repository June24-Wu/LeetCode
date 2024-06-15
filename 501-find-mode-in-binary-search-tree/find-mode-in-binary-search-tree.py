# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = collections.defaultdict(int)
        def dfs(node):
            nonlocal ans
            if not node:
                return
            ans[node.val] += 1
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        cout = 0 ; a = []
        for i in ans:
            if ans[i] > cout:
                a = [i]
                cout = ans[i]
            elif ans[i] == cout:
                a.append(i)
        return a
        