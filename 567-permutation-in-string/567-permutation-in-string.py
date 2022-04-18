class Solution:
    def checkInclusion(self, s2: str, s1: str) -> bool:
        if len(s2) > len(s1):return ""
        tableS2 = {}
        for i in s2:
            tableS2[i] = s2.count(i)
        tableS1 = {}
        for i in (s1+s2):
            tableS1[i] = 0
        
        def isValid():
            for i in tableS2.keys():
                if tableS1[i] != tableS2[i]:
                    return False
            return True
        
        for i in range(len(s2)):
            tableS1[s1[i]] += 1
        if isValid():
            return True
        p1 = 0 ; p2 = len(s2)
        while p2 < len(s1):
            # print(tableS1)
            tableS1[s1[p1]] -= 1
            p1 += 1
            tableS1[s1[p2]] += 1
            p2 += 1
            if isValid():
                return True
        return False
        