# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        
        def backtracking(left,right):
            if left > right:
                return [None]
            res = []
            for i in range(left,right + 1):
                leftnodes = backtracking(left,i-1)
                rightnodes = backtracking(i+1,right)
                for leftnode in leftnodes:
                    for rightnode in rightnodes:
                        node = TreeNode(i)
                        node.left = leftnode
                        node.right = rightnode
                        res.append(node)
            return res
        return backtracking(1,n)
        