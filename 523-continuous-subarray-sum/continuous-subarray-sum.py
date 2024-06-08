class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        nums[0] = nums[0] % k
        s = {0:-1}
        if nums[0] != 0:
            s[nums[0]] = 0
        for i in range(1,len(nums)):
            nums[i] = (nums[i] + nums[i-1]) % k
            if (nums[i] in s and i - s[nums[i]] > 1):
                return True
            if nums[i] not in s:
                s[nums[i]] = i
        # print(nums,s)
        return False
        