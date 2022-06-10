class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def sort(left,right,rank):
            if left >= right:
                return nums[left]
            p = left
            for i in range(left,right):
                if nums[i] < nums[right]:
                    nums[i] , nums[p] = nums[p] , nums[i]
                    p += 1
            nums[p] , nums[right] = nums[right] , nums[p]
            if right - p == rank - 1:
                return nums[p]
            elif right - p < rank - 1:
                return sort(left,p-1,rank-1-right+p)
            else:
                return sort(p+1,right,rank)
        return sort(0,len(nums)-1,k)
        