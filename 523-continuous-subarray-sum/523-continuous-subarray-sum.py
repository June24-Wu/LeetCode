class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        currRem, prevRem = 0, {}
        for i in range(len(nums)):
            currRem = (currRem + nums[i]) % k
            if currRem not in prevRem:
                prevRem[currRem] = i
            if (currRem == 0 and i > 0) or ((i - prevRem[currRem]) > 1):
                return True
        return False
            
            