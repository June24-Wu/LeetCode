class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        m = {}

        def reverse(num):
            return int("".join(list(str(num))[::-1]))
        ans = float("inf")
        for i , num in enumerate(nums):
            reverse_num = reverse(num)
            # print(num,reverse_num,m)
            if num in m:
                ans = min(ans,i - m[num])
            m[reverse_num] = i
        return -1 if ans == float("inf") else ans


        