# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        num = []
        def find(node):
            nonlocal num
            if not node:
                return
            find(node.left) 
            num.append(node.val)
            find(node.right)
        find(root)
        ans = {num[-1]:num[-1]}
        for i in range(len(num)-2,-1,-1):
            ans[num[i]] = num[i] + num[i+1]
            num[i] += num[i+1]
        def assign(node):
            nonlocal ans
            if not node:
                return None
            node.val = ans[node.val]
            node.left = assign(node.left)
            node.right = assign(node.right)
            return node
        return assign(root)

        