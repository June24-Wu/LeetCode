class Solution:
    def slowestKey(self, times: List[int], keysPressed: str) -> str:
        maxLength = 0; ans = "a"
        
        for idx , item in enumerate(times):
            item = item if idx == 0 else item - times[idx-1]
            if item >= maxLength:
                if item == maxLength:
                    ans = chr(max(ord(keysPressed[idx]) , ord(ans)))
                else:
                    maxLength = item
                    ans = keysPressed[idx]
        return ans
        