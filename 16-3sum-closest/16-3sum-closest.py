class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("inf")
        ans = None
        
        
        def isSmall(val):
            nonlocal diff
            nonlocal target
            nonlocal ans
            if abs(val - target) < diff:
                diff = abs(val - target)
                ans = val
            return
        for index in range(0,len(nums)):
            if diff == 0:
                return target
            i = index + 1
            j = len(nums) - 1
            while i < j:
                sum3 = nums[index] + nums[i] + nums[j]
                isSmall(sum3)
                if sum3 < target:
                    i += 1
                else:
                    j -= 1
        # print(ans)
        return ans
                    
                
        