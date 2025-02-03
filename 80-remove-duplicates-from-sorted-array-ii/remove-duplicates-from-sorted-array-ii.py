class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0; cnt = collections.defaultdict(int)
        for num in nums[:]:
            cnt[num] += 1
            if cnt[num] <= 2:
                nums[left] = num
                left += 1
        return left
            
        