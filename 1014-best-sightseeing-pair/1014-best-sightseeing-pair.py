class Solution:
    def maxScoreSightseeingPair(self, v: List[int]) -> int:
        ans = - float("inf") ; curr_max = - float("inf")
        for idx , item in enumerate(v):
            val = item - idx
            ans = max(ans,curr_max + val)
            curr_max = max(curr_max,item + idx)
        return ans
            
        
        
            
        