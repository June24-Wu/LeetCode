# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root == None:return root
        return_li = []
        sub_li = [root.val]
        def dfs(node,target):
            if node.left == None and node.right == None:
                if target == 0:
                    return_li.append(sub_li[:])
                return
            if node.left != None:
                sub_li.append(node.left.val)
                dfs(node.left,target-node.left.val)
                sub_li.pop()
                
            if node.right != None:
                sub_li.append(node.right.val)
                dfs(node.right,target-node.right.val)
                sub_li.pop()
                
        dfs(root,targetSum - root.val)
        return return_li
            
                
                
        