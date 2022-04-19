# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        nodeList = []
        def dfs(node):
            if node == None:return
            dfs(node.left)
            nodeList.append(node.val)
            dfs(node.right)
        dfs(root)
        # print(nodeList)
        def dfs2(node):
            if node == None:
                return
            dfs2(node.left)
            index = nodeList.index(node.val)
            node.val += sum(nodeList[index+1:])
            dfs2(node.right)
            return node
        return dfs2(root)
        # print(nodeList)
            
        