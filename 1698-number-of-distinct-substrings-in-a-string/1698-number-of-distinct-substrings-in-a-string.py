class Solution:
    def countDistinct(self, s):
        n, dict1, total = len(s), {}, 0

        for i in range(n):
            for j in range(i+1,n+1):
                if s[i:j] not in dict1:
                    dict1[s[i:j]] = 1
                    total += 1
                else:
                    continue

        return total