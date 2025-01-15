class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ca = collections.defaultdict(int) ; cb = collections.defaultdict(int)
        ans = [] ; curr = 0 ; c = collections.defaultdict(int)
        for i , j in zip(A,B):
            ca[i] += 1 ; cb[j] += 1
            if min(ca[i],cb[i]) > c[i]:
                c[i] = min(ca[i],cb[i])
                curr += 1
            if min(ca[j],cb[j]) > c[j]:
                c[j] = min(ca[j],cb[j])
                curr += 1    
            ans.append(curr)
        return ans
        