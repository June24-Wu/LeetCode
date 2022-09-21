class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = 0
        for i in nums:
            if i % 2 == 0:
                ans += i
        res = []
        for val , idx in queries:
            if nums[idx] % 2== 0 and val % 2== 0:
                ans += val
            elif nums[idx] % 2 == 0 and val % 2 != 0:
                ans -= nums[idx]
            elif nums[idx] % 2 != 0 and val % 2 != 0:
                ans += nums[idx] + val
            nums[idx]+=val
            res.append(ans)
        return res
        