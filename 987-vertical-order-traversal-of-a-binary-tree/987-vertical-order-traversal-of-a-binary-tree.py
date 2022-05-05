# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(node,row,col):
            if node == None:return
            nonlocal res
            res.append((col,row,node.val))
            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)
            return
        dfs(root,0,0)
        res.sort()

        ans = [] ; index = None
        for col , row , val in res:
            if col != index:
                index = col
                ans.append([])
            ans[-1].append(val)

        return ans
        