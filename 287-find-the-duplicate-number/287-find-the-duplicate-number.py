class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # table = {}
        # for i in nums:
        #     if i in table.keys():
        #         return i
        #     else:
        #         table[i] = 1

        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = nums[0]
        slow = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow