class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        dp = [False] * len(nums)
        dp[0] = nums[0]
        last_index = len(nums) - 1
        for idx in range(len(nums)):
            # print(dp)
            if dp[idx] == False:
                return False
            for step in range(1,nums[idx] + 1):
                get_to = idx + step
                if get_to == last_index:
                    return True
                # print(get_to)
                dp[get_to] = True
            
        return False
            