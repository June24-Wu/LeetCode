# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, p: List[int]) -> Optional[TreeNode]:
        def dfs(l,r):
            if p == []:
                return None
            val = p[0]
            if l < val < r:
                node = TreeNode(p.pop(0))
                node.left = dfs(l,node.val)
                node.right = dfs(node.val,r)
                return node
            else:
                return None
        return dfs( - float("inf") , float("inf"))
        # print()
        