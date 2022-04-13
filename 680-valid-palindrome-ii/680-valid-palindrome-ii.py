class Solution:
    def validPalindrome(self, s: str) -> bool:
        li = list(s)
        def isPalindrome(left,right):
            if left >= right: return True
            return isPalindrome(left+1,right-1) and s[left] == s[right]
        

        left = 0 ; right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(left,right-1) or isPalindrome(left+1,right)
        return True
        
    
        
        