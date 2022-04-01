# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        a = self.__rob(root)
        return max(a[1],a[0])
        
        
        
    def __rob(self,node):
        if not node:return (0,0)  # steal , not steal
        
        val = node.val
        left = self.__rob(node.left) # (steal,not steal)
        right = self.__rob(node.right) # (steal,not steal)
        
        steal = val + left[1] + right [1]
        not_steal = max(left[0],left[1]) + max(right[0],right[1])
        
        return (steal,not_steal)
        
        
        # hashmap = {}
        # def __rob(root: Optional[TreeNode]) -> int:
        #     if not root: return 0
        #     if root in hashmap.keys():return hashmap[root]
        #     robVal = root.val
        #     if root.left:
        #         robVal += __rob(root.left.left) + __rob(root.left.right)
        #     if root.right:
        #         robVal += __rob(root.right.left) + __rob(root.right.right)
        #     not_rob = __rob(root.left) + __rob(root.right)
        #     maxVal = max(robVal,not_rob)
        #     hashmap[root] = maxVal
        #     return maxVal
        # return __rob(root)
        
        