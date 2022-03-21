# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:return None
        stack = [root]
        return_li = []
        sub_return = []
        size = len(stack)
        cnt = 0
        
        while stack != []:
            a = stack.pop(0)
            if a.left != None:
                stack.append(a.left)
            if a.right != None:
                stack.append(a.right)   
            sub_return.append(a.val)
            cnt += 1
            if cnt == size:
                return_li.append(max(sub_return))
                sub_return = []
                size = len(stack)
                cnt = 0
        return return_li