class Node:
    def __init__(self,val, parent = None):
        self.val = val
        self.parent = parent
        self.kids = []
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        table = {}
        for i in range(len(pid)):
            parent = ppid[i] ; kid = pid[i]
            if parent not in table:
                table[parent] = Node(val = parent)
            if kid not in table:
                table[kid] = Node(val = kid)
            table[parent].kids.append(table[kid])
        ans = []
        def dfs(node):
            nonlocal ans
            ans.append(node.val)
            for i in node.kids:
                dfs(i)
            return
        dfs(table[kill])
        return ans