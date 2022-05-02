# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        li = []
        def dfs(node):
            nonlocal li
            if node == None:
                return
            dfs(node.left)
            li.append(node.val)
            dfs(node.right)
            return
        dfs(root)
        res = TreeNode(0)
        p = res
        for i in range(len(li)):
            p.right = TreeNode(li[i])
            p = p.right
        return res.right
        