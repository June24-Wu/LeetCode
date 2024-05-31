class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums = Counter(nums)
        a = []
        for i in nums:
            if nums[i] == 1:
                a.append(i)
        return a
        