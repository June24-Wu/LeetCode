# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        
        def dfs(left,right):
            if preorder == [] or left > right:
                return None
            val = preorder.pop(0)
            if left == right:
                return TreeNode(val)
            index = inorder.index(val)
            node = TreeNode(val)
            node.left = dfs(left,index - 1)
            node.right = dfs(index + 1,right)
            return node
        return dfs(0,len(inorder) - 1)
        