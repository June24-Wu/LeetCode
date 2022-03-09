# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:return None
        li = []
        def dfs(node):
            if node == None:return None
            dfs(node.left)
            li.append(node.val)
            dfs(node.right)
            return
        dfs(root)
        total = sum(li)
        table = {}
        table[li[0]] = total
        for i in range(1,len(li)):
            total -= li[i-1]
            table[li[i]] = total
        def dfs2(node):
            if node == None:return None
            dfs2(node.left)
            node.val = table[node.val]
            dfs2(node.right)
            return node
        dfs2(root)
        return root
        