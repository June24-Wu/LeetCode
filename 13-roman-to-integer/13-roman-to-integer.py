class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        ans = 0
        for index,item in enumerate(s):
            if index < len(s) - 1 and table[item] < table[s[index+1]]:
                ans -= table[item]
            else:
                ans += table[item]
        print(ans)
        return ans
        