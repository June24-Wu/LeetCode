class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        m = collections.defaultdict(dict)
        for (i , j) , char in zip(points,list(s)):
            v = max(abs(i),abs(j))
            m[char][v] = m[char][v] + 1 if v in m[char] else 1
        minval = float("inf")
        for char in m:
            li = list(m[char].keys())
            li.sort()
            flag = False
            for length in li:
                if m[char][length] >= 2:
                    
                    minval = min(minval,length-1)
                    break
                else:
                    if not flag:
                        flag = True
                    else:
                        minval = min(minval,length-1)
        ans = 0
        
        for char in m:
            li = list(m[char].keys())
            li.sort()
            if li[0] <= minval:
                # print(char,m[char])
                ans += 1
        # print(minval)
        return ans
        