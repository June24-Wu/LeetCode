class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        curr = 0 ; m = collections.defaultdict(int) ; m[0] = 1
        for idx , i in enumerate(nums):
            curr += i
            nums[idx] = curr % k
            ans += m[nums[idx]]
            m[nums[idx]] += 1
        return ans
        