class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # kadane max(max_pre * curr , cur)
        
        ans = max(nums) ; mincurr = nums[0] ; maxcurr = nums[0]
        for i in range(1,len(nums)):
            curr = nums[i]
            temp_mincurr = min(curr,mincurr * curr , maxcurr * curr)
            maxcurr = max(curr,maxcurr * curr , mincurr * curr)
            mincurr = temp_mincurr
            ans = max(ans,maxcurr)
        return ans