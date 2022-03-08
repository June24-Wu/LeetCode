# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        hashmap = {}
        def __rob(root: Optional[TreeNode]) -> int:
            if not root: return 0
            if root in hashmap.keys():return hashmap[root]
            robVal = root.val
            if root.left:
                robVal += __rob(root.left.left) + __rob(root.left.right)
            if root.right:
                robVal += __rob(root.right.left) + __rob(root.right.right)
            not_rob = __rob(root.left) + __rob(root.right)
            maxVal = max(robVal,not_rob)
            hashmap[root] = maxVal
            return maxVal
        return __rob(root)
        
        