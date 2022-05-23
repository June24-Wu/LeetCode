class Solution:
    def frequencySort(self, s: str) -> str:
        temp = []
        s = list(s)
        for i in set(s):
            temp.append((i,s.count(i)))
        temp.sort(key = lambda x: - x[1])
        ans = ""
        for char , cnt in temp:
            ans += char * cnt
        return ans
        