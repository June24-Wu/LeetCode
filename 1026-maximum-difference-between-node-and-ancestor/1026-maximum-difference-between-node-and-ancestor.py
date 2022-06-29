# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # return : (maxDifference , minVal , maxVal , )
        
        def dfs(node):
            if node == None:
                return (0,float("inf") , - float("inf"))
            if node.left == None and node.right == None:
                return (0,node.val,node.val)
            leftDiff , leftMin , leftMax = dfs(node.left)
            rightDiff , rightMin , rightMax = dfs(node.right)
            minVal = min(leftMin,rightMin)
            maxVal = max(leftMax , rightMax)
            diff = max(abs(node.val - minVal) , abs(node.val - maxVal))
            diff = max(diff,leftDiff,rightDiff)
            minVal = min(minVal , node.val)
            maxVal = max(maxVal , node.val)
            # print(node.val , diff , minVal , maxVal)
            return (diff,minVal,maxVal)
        diff , minVal , maxVal = dfs(root)
        return diff
        