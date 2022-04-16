# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        final = {}
        def dfs(node):
            if node == None:return 0 
            nonlocal final
            # if node.left == None and node.right == None: # is leaf
            #     if node.val not in final.keys():
            #         final[node.val] = 0
            #     final[node.val] += 1
            #     return node.val
            left = dfs(node.left)
            right = dfs(node.right)
            print(left,right,node.val)
            val = node.val + left + right
            if val not in final.keys():
                final[val] = 0
            final[val] += 1
            return val
        dfs(root)
        print(final)
        maxFrequency = 0
        for i in final.keys():
            maxFrequency = max(final [i],maxFrequency)
        final_list = []
        for i in final.keys():
            if final[i] == maxFrequency:
                final_list.append(i)
        return final_list
        