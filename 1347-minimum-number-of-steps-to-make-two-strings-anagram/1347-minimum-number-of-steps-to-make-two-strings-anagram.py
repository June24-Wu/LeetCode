class Solution:
    def minSteps(self, s: str, t: str) -> int:
        table1 = collections.defaultdict(int)
        table2 = collections.defaultdict(int)
        for i in s:
            table1[i] += 1
        for i in t:
            table2[i] += 1
            ans = 0
        for i in table2:
            ans += max(0,table2[i] - table1[i])
        return ans
        # print(table1)
        # print(table2)