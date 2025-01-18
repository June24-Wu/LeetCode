class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        results = [] ; n = len(nums)
        for idx , i in enumerate(nums):
            results.append(nums[(idx + i) % n ])
        return results