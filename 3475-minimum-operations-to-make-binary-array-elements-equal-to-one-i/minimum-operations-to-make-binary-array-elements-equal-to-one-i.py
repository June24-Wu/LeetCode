class Solution:
    def minOperations(self, nums: List[int]) -> int:
        h = []
        def flip(v,times):
            times = times % 2
            if times == 0:
                return v
            else:
                return 0 if v == 1 else 1
        ans = 0
        for idx, i in enumerate(nums[:-2]):
            while h and h[0] <= idx - 3:
                h.pop(0)
            i = flip(i,len(h))
            if i == 0:
                ans += 1
                h.append(idx)
            # print(idx,h,i,ans)
        for idx in range(len(nums)-2,len(nums)):
            while h and h[0] <= idx - 3:
                h.pop(0)
            i = flip(nums[idx],len(h))
            # print(idx,h,i)
            if i == 0:
                return -1
        return ans
        