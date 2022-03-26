class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        cnt = 0
        p1 = len(g) - 1
        p2 = len(s) - 1
        
        while p1 >= 0 and p2 >=0:
            if g[p1] > s[p2]:
                p1 -= 1
                continue
            else:
                p1 -= 1
                p2 -=1
                cnt +=1

        return cnt
        