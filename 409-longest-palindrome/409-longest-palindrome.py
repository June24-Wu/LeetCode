class Solution:
    def longestPalindrome(self, s: str) -> int:
        array = [(i,s.count(i)) for i in set(list(s))]
        array.sort(key = lambda x : - x[1])
        print(array)
        maxodd = None
        ans = 0
        for char , cnt in array:
            if cnt % 2 == 0:
                ans += cnt
            if cnt % 2 == 1:
                if maxodd == None:
                    maxodd = char
                    ans += cnt
                else:
                    ans += cnt - 1
        return ans
        