class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        index1 = nums.index(min(nums))
        index2 = nums.index(max(nums))
        left = min(index1,index2); right = max(index1,index2)
        return min(right+1,len(nums)-left,left+1+len(nums)-right)
        