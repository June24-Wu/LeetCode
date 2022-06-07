# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        table = set()
        ans = {}
        def dfs(node):
            nonlocal table
            nonlocal ans
            if node == None:
                return "#"
            left = dfs(node.left)
            right = dfs(node.right)
            text = str(node.val) + "," + left + "," + right
            if text in table:
                ans[text] = node
            table.add(text)
            return text
        dfs(root)
        # print(ans)
        return [ans[i] for i in ans]
        