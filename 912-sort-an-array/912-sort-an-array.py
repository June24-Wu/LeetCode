class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def sort(left,right): # inclued
            if left >= right:
                return
            mid = (left + right) // 2
            nums[mid] , nums[right] = nums[right] , nums[mid]
            num = nums[right] ; p1 = left ; p2 = right - 1 ; p = left
            while p1 != p2:
                if nums[p1] < num:
                    p1 += 1
                else:
                    nums[p1] , nums[p2] = nums[p2] , nums[p1]
                    p2 -= 1
            if nums[p1] < num:
                p1 += 1
            nums[p1] , nums[right] = nums[right] , nums[p1]
            sort(left,p1-1) ; sort(p1 + 1,right)
        sort(0,len(nums)-1)
        return nums
            
            