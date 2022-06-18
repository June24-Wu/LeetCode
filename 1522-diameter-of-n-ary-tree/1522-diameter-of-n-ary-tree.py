"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        ans = 0
        def dfs(node):
            nonlocal ans
            if node.children == []:
                ans = max(ans,1)
                return 1
            lengthList = []
            for i in node.children:
                lengthList.append(dfs(i))
            if len(lengthList) == 1:
                ans = max(ans,lengthList[0] + 1)
            else:
                lengthList.sort(reverse = True)
                ans = max(sum(lengthList[:2])+1,ans)
            # print(node.val , "  ",lengthList)
            # print(node.children)
            return lengthList[0] + 1
        dfs(root)
        # print(ans)
        return ans - 1
            
                
            
            