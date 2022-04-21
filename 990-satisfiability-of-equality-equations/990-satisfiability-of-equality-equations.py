class Solution:
    class UnionFind:
        def __init__(self):
            self.parent = [i for i in range(26)]
        def find(self,x:int):
            if x == self.parent[x]:
                return x
            else:
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
        def union(self,x:int,y:int):
            self.parent[self.find(x)] = self.find(y)
    def equationsPossible(self, equations: List[str]) -> bool:
        unionfind = self.UnionFind()
        for i in equations:
            if i[1] == "=":
                x = ord(i[0]) - ord("a")
                y = ord(i[3]) - ord("a")
                unionfind.union(x,y)
        for i in equations:
            if i[1] == "!":
                x = ord(i[0]) - ord("a")
                y = ord(i[3]) - ord("a")
                if unionfind.find(x) == unionfind.find(y):
                    return False
        return True
        