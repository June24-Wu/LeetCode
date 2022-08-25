class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        newnums = [None] * len(nums)
        for idx , item in enumerate(nums):
            char = str(item) * (20 // len(str(item)) + 1)
            newnums[idx] = (char,idx)
        newnums.sort()
        # print(nums,newnums)
        ans = ""
        for i in range(len(newnums) - 1,-1,-1):
            # print(newnums[1])
            ans += str(nums[newnums[i][1]])
        return str(int(ans))