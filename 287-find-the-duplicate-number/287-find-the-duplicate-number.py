class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = nums[0] ; fast = nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = nums[slow]
        fast = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        # slow = nums[0]
        # fast = nums[nums[0]]
        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        # fast = nums[0]
        # slow = nums[slow]
        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[fast]
        # return slow