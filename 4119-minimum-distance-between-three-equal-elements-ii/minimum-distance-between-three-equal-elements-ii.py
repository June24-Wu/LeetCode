class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        m = collections.defaultdict(list)


        ans = float("inf")
        for idx , i in enumerate(nums):
            if len(m[i]) >= 2:
                val1 = m[i][-2]
                val2 = m[i][-1]
                ans = min(ans,idx - val2 + idx - val1 + val2 - val1)
            m[i].append(idx)
        return ans if ans != float("inf") else -1
        