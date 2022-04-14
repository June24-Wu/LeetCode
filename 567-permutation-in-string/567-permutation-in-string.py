class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        checkTable = {}
        for i in set(list(s2)):
            checkTable[i] = 0
        for i in s1:
            if i not in checkTable.keys():
                checkTable[i] = 0
            checkTable[i] += 1
        
        p1 = 0; p2 = len(s1) - 1
        
        s2Table = {}
        for i in set(list(s2)):
            s2Table[i] = 0
        for i in range(0,p2+1):
            s2Table[s2[i]] += 1
        if s2Table == checkTable: return True
        # print(s2Table)
        while p2 < len(s2) - 1:
            s2Table[s2[p1]] -= 1
            p1 += 1
            p2 += 1
            s2Table[s2[p2]] += 1
            # print(s2Table)
            if s2Table == checkTable: return True
        return False

                
        