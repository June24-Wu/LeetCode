# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        final = 0
        def dfs(node):
            nonlocal final
            # [isBinaryTree,minValue,maxValue,sumVal]
            if node == None: return [1,float("inf"),-float("inf"),0]
            
            leftTree = dfs(node.left)
            rightTree = dfs(node.right)
            res = [0 for _ in range(4)]
            if leftTree[0] == 1 and rightTree[0] == 1 and node.val > leftTree[2] and node.val < rightTree[1]:
                res[0] = 1 ; res[1] = min(node.val,leftTree[1]) ; res[2] = max(node.val,rightTree[2])
                res[3] = node.val + leftTree[3] + rightTree[3]
                final = max(final,res[3])
            return res
        dfs(root)
        return final