class UF:
    def __init__(self,n):
        self.li = [i for i in range(n)]
    def find(self,idx):
        if idx != self.li[idx]:
            return self.find(self.li[idx])
        else:
            return idx
    def union(self,a,b):
        self.li[self.find(a)] = self.find(b)
        return
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for u, v in edges:
            uf.union(u,v)
        ans = collections.defaultdict(list)
        for i in range(n):
            ans[uf.find(i)].append(i)
        rt = 0
        for value in ans.values():
            isValid = True
            for i in range(len(value)):
                for j in range(i+1,len(value)):
                    if [value[i],value[j]] not in edges and [value[j],value[i]] not in edges:
                        isValid = False
            if isValid:
                rt += 1
        return rt
            

        