class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        l1 = [0 for _ in range(26)]
        l2 = [0 for _ in range(26)]
        for i in s :
            l1[ord(i) - ord("a")] += 1
        for i in t:
            l2[ord(i) - ord("a")] += 1
        return l1 == l2
        

        