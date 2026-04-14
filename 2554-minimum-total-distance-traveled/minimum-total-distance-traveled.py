class Solution:
    def minimumTotalDistance(self, A: List[int], B: List[List[int]]) -> int:
        A.sort();B.sort()
        @lru_cache(None)
        def dp(i,j,k):
            if i == len(A):
                return 0
            if j == len(B):
                return float("inf")
            a1 = dp(i+1,j,k+1) + abs(A[i] - B[j][0]) if k < B[j][1] else float("inf")
            a2 = dp(i,j+1,0)
            return min(a1,a2)
        return dp(0,0,0)
            
            
        