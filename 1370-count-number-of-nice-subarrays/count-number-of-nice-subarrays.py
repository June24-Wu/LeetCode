class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums) ; curr = 0 ; ans = 0
        cnt = collections.defaultdict(int)
        cnt[0] = 1
        for i in range(n):
            if nums[i] % 2 != 0:
                curr += 1
            # print(cnt,curr)
            cnt[curr] += 1
            ans += cnt[curr-k]
        # print(dp)
        return ans
        