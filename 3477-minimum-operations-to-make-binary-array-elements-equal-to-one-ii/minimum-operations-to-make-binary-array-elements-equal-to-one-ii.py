class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        flips = 0
        flipped = False
        
        for i in range(n):
            # Determine the actual value considering the flip state
            actual_value = nums[i] if not flipped else 1 - nums[i]
            
            if actual_value == 0:
                # Flip the state starting from this point
                flips += 1
                flipped = not flipped
        
        return flips
            