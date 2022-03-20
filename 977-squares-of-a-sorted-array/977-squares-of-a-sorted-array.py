class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new = []
        for i in nums:
            new.append(i*i)
        new.sort()
        return new
        