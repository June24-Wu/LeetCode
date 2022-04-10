class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        arr = [0 for _ in range(len(nums))]
        
        def cnt(num):
            for i in range(len(nums)):
                arr[i] = nums[i] // num + 1 if nums[i] % num != 0 else nums[i] // num
            return sum(arr)
        
        
        
        left , right =  1 , max(nums)
        
        while left <= right:
            mid = (left + right) // 2
            
            if cnt(mid) <= threshold:
                right = mid - 1
            else:
                left = mid + 1
        return left
        