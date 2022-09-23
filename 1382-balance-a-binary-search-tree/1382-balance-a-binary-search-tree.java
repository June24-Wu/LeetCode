# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        li = []
        
        def dfs(node):
            nonlocal li
            if not node:
                return
            dfs(node.left)
            li.append(node.val)
            dfs(node.right)
            return
        dfs(root)
        def build(left,right):
            if left > right:
                return None 
            if left == right:
                return TreeNode(li[left])
            mid = (left+right) // 2
            node = TreeNode(li[mid])
            node.left = build(left,mid-1)
            node.right = build(mid+1,right)
            return node
        return build(0,len(li)-1)