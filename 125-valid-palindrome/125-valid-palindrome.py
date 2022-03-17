class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =''.join(x for x in s if x.isalnum())
        s = s.lower()
        left = 0
        right = len(s)-1
        # if len(s) == 1:return False
        while right >= left:
            if s[right] == s[left]:
                left += 1
                right -= 1
            else:
                return False
        return True

        