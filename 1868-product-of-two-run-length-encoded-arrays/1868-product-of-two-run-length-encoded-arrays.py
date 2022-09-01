class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        ans = []
        p1 = 0 ; p2 = 0
        while p1 < len(encoded1) and p2  < len(encoded2):
            val1 , cnt1 = encoded1[p1]
            val2 , cnt2 = encoded2[p2]
            if cnt1 == cnt2:
                ans.append([val1*val2,cnt1])
                p1 += 1; p2 += 1
            elif cnt1 < cnt2:
                ans.append([val1*val2,cnt1])
                encoded2[p2][1] -= cnt1
                p1 += 1
            else:
                ans.append([val1*val2,cnt2])
                encoded1[p1][1] -= cnt2
                p2 += 1
        res = []
        while ans:
            item = ans.pop(0)
            if not res or res[-1][0] != item[0]:
                res.append(item)
            else:
                res.append([item[0],item[1] + res.pop()[1]])
        return res
            
        