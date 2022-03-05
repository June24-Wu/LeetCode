class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s2 = '#'
        for i in s:
            s2  = s2 + i + "#"
        result = 0
        print(s2)
        for i in range(len(s2)):
            if s2[i] == "#":
                left, right = i - 1, i + 1
                while left >= 0 and right < len(s2):
                    left_val, right_val = s2[i - 1] , s2[i + 1]
                    if left_val == right_val:
                        break
                    if s2[left] == "#" and s2[right] == "#":
                        left -= 1
                        right += 1
                    elif s2[left] == left_val and right_val == s2[right]:
                        left -=1
                        right +=1
                    else:
                        break
                if right - i > 1:
                    result += round((right - i -1) / 2)
        return result
                
            
        