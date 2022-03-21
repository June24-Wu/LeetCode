# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:return root
        stack = [root]
        size = len(stack)
        cnt = 0
        return_li = []
        layer = []
        while stack != []:
            a = stack.pop(0)
            layer.append(a.val)
            if a.left != None:
                stack.append(a.left)
            if a.right != None:
                stack.append(a.right)
            cnt+=1
            if cnt == size:
                cnt = 0
                size = len(stack)
                return_li.append(layer[-1])
                layer = []
        return return_li
                