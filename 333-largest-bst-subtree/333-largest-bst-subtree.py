# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if node == None:
                return (True,0,float("inf") ,  - float("inf"))
            isLeft , leftSize , small , leftB = dfs(node.left)
            isRight , rightSize , rightB , big = dfs(node.right)
            if isLeft and isRight and leftB < node.val < rightB:
                cnt = leftSize + rightSize + 1
                self.ans = max(self.ans,cnt)
                return (True,cnt,min(small,node.val),max(node.val,big))
            else:
                return (False,0,0,0)
        dfs(root)
        return self.ans
                
            
        