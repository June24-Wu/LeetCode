class Solution:
    def longestDupSubstring(self, s: str) -> str:
        li = [ord(i) - ord("a") for i in s]
        def rabinCarp(n):
            a = 26 ; mod = 10**9 + 7 ; aL = pow(a,n,mod) ; code = 0 ; visited = collections.defaultdict(list)
            for i in range(n):
                code = (code * a + li[i]) % mod
            visited[code].append(s[:n])
            for i in range(n,len(li)):
                code = (code * a - li[i - n] * aL + li[i]) % mod
                if code in visited:
                    for char in visited[code]:
                        if char == s[i + 1 - n : i + 1]:
                            return char
                visited[code].append(s[i + 1 - n : i + 1])
            return ""
        left = 1 ; right = len(s)
        while left < right:
            mid = (left + right) // 2 + 1
            rabincarp = rabinCarp(mid)
            if rabincarp == "":
                right = mid - 1
            else:
                left = mid
        return "" if rabinCarp(left) == "" else rabinCarp(left)
        
                
                
        