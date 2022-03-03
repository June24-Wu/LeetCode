class Solution:
    def longestPalindrome(self, s: str) -> int:
        mid , max_even = None,0
        table = {}
        for i in s:
            table[i] = table[i] + 1 if i in table.keys() else 1
            value = table[i]
            if value % 2 == 0:
                max_even += 2
        for i in s:
            if table[i] % 2 == 1:
                return max_even + 1
        return max_even
                
        
        