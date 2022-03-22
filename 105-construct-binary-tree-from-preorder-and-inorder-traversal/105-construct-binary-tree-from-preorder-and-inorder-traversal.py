# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        table = {val:idx for idx , val in enumerate(inorder)}
        def dfs(inorder_left,inorder_right):
            if inorder_left > inorder_right:
                return None
            val = preorder.pop(0)
            index = table[val]
            root = TreeNode(val)
            if inorder_left == inorder_right:
                return root
            root.left = dfs(inorder_left,index-1)
            root.right = dfs(index+1,inorder_right)
            return root
        return dfs(0,len(inorder)-1)