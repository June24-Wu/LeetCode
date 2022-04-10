class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sort(left,right):
            mid = random.randint(left,right)
            mid_num = nums[mid]
            nums[mid] , nums[right] = nums[right] , nums[mid]
            
            p = left
            
            for i in range(left,right):
                if nums[i] < mid_num:
                    nums[i] , nums[p] = nums[p] , nums[i]
                    p += 1
            
            nums[p] , nums[right] =  nums[right] , nums[p]
            return p
        
        def sort2(l,r):
            if l >= r:return
            mid = sort(l,r)
            sort2(mid+1,r)
            sort2(l,mid-1)
        
        sort2(0,len(nums)-1)
        
        return nums
            
        