class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        m = collections.defaultdict(list)

        ans = float("inf")
        for idx in range(len(nums)):
            if len(m[nums[idx]]) >= 2:
                val1 = m[nums[idx]][-2]
                val2 = m[nums[idx]][-1]
                ans = min(ans,idx - val1 + idx - val2 + val2 - val1)
            m[nums[idx]].append(idx)
            # print(m)
        return ans if ans != float("inf") else -1
            
        