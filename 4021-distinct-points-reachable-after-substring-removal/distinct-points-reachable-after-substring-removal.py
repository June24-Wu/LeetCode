class Solution:
    def distinctPoints(self, s: str, k: int) -> int:

        ans = set()
        # ans.add((0,0))

        curr_x = 0; curr_y = 0

        def add(char):
            nonlocal curr_x
            nonlocal curr_y
            if char == "U":
                curr_y += 1
            elif char == "D":
                curr_y -= 1
            if char == "L":
                curr_x -= 1
            elif char == "R":
                curr_x += 1
        def reverse(char):
            nonlocal curr_x
            nonlocal curr_y
            if char == "U":
                curr_y -=1
            elif char == "D":
                curr_y += 1
            if char == "L":
                curr_x += 1
            elif char == "R":
                curr_x -= 1
        
        for i in range(k):
            add(s[i])
        ans.add((curr_x,curr_y))

        for i in range(k,len(s)):
            reverse(s[i-k])
            add(s[i])
            ans.add((curr_x,curr_y))

        # print(ans)
        return len(ans)



        return 2
        