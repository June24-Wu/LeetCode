class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        table = set()
        for i in range(len(s) - k + 1):
            table.add(s[i:i+k])
        # print(table)
        return len(table) == 2 ** k
        