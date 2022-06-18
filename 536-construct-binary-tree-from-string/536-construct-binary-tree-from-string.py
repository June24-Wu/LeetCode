# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if s == "":
            return None
        s = list(s)
        def dfs():
            sign = 1
            val = 0
            while s and s[0] not in ["(",")"]:
                pop = s.pop(0)
                if pop == "-":
                    sign = - 1
                elif pop.isdigit():
                    val = val * 10 + int(pop)
            node = TreeNode(val * sign)
            if s and s[0] == ")":
                return node
            if s and s[0] == "(":
                s.pop(0)
                node.left = dfs()
                s.pop(0)
            if s and s[0] == "(":
                s.pop(0)
                node.right = dfs()
                s.pop(0)
            return node
        return dfs()
            
            
        