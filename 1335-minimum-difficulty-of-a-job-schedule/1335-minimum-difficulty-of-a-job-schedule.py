class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
        if d == len(jobDifficulty):
            return sum(jobDifficulty)
        n = len(jobDifficulty)
        ans = float("inf")
        path = 0
        @cache
        def backtracking(index,day,curr):
            nonlocal path ; nonlocal ans
            if index == n:
                if day == d + 1:
                    return 0
                return float("inf")
            if day > d:
                return float("inf")
            val = max(jobDifficulty[index],curr)
            res = min(val + backtracking(index+1,day+1,0),backtracking(index+1,day,val))
            return res
        return backtracking(0,1,0)
            
            
            
            
            
            
        