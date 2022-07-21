class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {0:1}
        ans = cum_sum = 0
        for i,num in enumerate(nums):
            cum_sum += num
            rem = cum_sum % k
            if rem < 0:
                rem += k
            if rem in d:
                ans += d[rem]
                d[rem] += 1
            else:
                d[rem] = 1
        return ans
        