# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def getHeight(node):
            if node == None: return 0
            return max(getHeight(node.left) , getHeight(node.right)) + 1
        height = getHeight(root)
        treeList = [["" for _ in range(2**height - 1)] for _ in range(height)]
        m = len(treeList)
        n = len(treeList[0])
        height -= 1
        def dfs(node,row,column):
            row = int(row)
            column= int(column)
            nonlocal treeList
            if row >= len(treeList) or node == None: return
            treeList[row][column] = str(node.val)
            dfs(node.left,row+1,column - 2**(height-row-1))
            dfs(node.right,row+1,column + 2**(height-row-1))
            return
        dfs(root,0,(n-1)/2)
        return treeList
        