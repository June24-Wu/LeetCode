class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            target_value = target - nums[i]
            if target_value in a.keys():
                return [a[target_value],i]
            else:
                a[nums[i]] = i
        return None
        