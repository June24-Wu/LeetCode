# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:return root
        final = []
        sub_final = []
        stack = [root]
        cnt = 0
        size = len(stack)
        
        # --------1
        # while stack != []:
        #     sub_final = []
        #     for i in stack:
        #         sub_final.append(i.val)
        #     final.append(sub_final)
        #     new_stack = stack.copy()
        #     stack = []
        #     while new_stack != []:
        #         a = new_stack.pop(0)
        #         if a.left != None:
        #             stack.append(a.left)
        #         if a.right != None:
        #             stack.append(a.right)
        # return final
        
        
        # --------2
        while stack != []:
            a = stack.pop(0)
            sub_final.append(a.val)
            if a.left != None:
                stack.append(a.left)
            if a.right != None:
                stack.append(a.right)
            cnt += 1
            if cnt == size:
                final.append(sub_final)
                sub_final = []
                size = size = len(stack)
                cnt = 0
        return final
            
                
            
        