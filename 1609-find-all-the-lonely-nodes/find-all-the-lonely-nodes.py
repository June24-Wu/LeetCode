# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def isLeaf(node):
            nonlocal ans
            if not node:
                return None
            if not node.left and not node.right:
                return node.val
            left = isLeaf(node.left)
            right = isLeaf(node.right)
            if not left and right:
                ans.append(right)
                return node.val
            if not right and left:
                ans.append(left)
                return node.val
            if not left and not right:
                return node.val
            if left and right:
                return node.val
        isLeaf(root)
        return ans

            
        