class Node:
    def __init__(self,val,parent = None):
        self.parent = parent
        self.val = val
        self.kids = []
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        table = {}
        for group in regions:
            parent = group[0]
            table[parent] = Node(val = parent) if parent not in table else table[parent]
            for idx in range(1,len(group)):
                kid = Node(val = group[idx] , parent = table[parent])
                table[group[idx]] = kid
                table[parent].kids.append(kid)
        for i in table:
            if table[i].parent == None:
                root = table[i]
        def dfs(node):
            if node.val in [region1, region2]:
                return node
            if node.kids == []:
                return None
            cnt = 0
            ans = None
            for i in node.kids:
                if dfs(i):
                    cnt += 1
                    ans = dfs(i)
            if cnt == 1:
                return ans
            if cnt > 1:
                return node
            return None
        # print()
        return dfs(root).val
                
        