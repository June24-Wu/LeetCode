# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dfs(left,right):
            if left > right:
                return None
            node = preorder.pop(0)
            node = TreeNode(node)
            if left == right:
                return node
            idx = inorder.index(node.val)
            node.left = dfs(left,idx - 1)
            node.right = dfs(idx+1,right)
            return node
        return dfs(0,len(inorder) - 1)
        