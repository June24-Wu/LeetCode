# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q:
            return 0
        ans = -1
        def dfs(node):
            nonlocal ans
            if not node:
                return -1
            # print(node.val,ans)
            left = dfs(node.left)
            right = dfs(node.right)
            if ans != -1:
                # print(ans)
                return ans
            # print(node.val,left,right)
            if node.val == p or node.val == q:
                if left != -1 or right != -1:
                    ans = max(left+1,right+1)
                    return ans
                else:
                    return 0
            elif left != -1 and right != -1:
                ans = left + right + 2
                return ans
            elif left != -1:
                return left + 1 
            elif right != -1:
                return right + 1
            else:
                return -1
        return dfs(root)

            
            
            
        