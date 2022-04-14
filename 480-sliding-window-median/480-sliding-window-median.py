class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def median(array):
            array.sort()
            if len(array) % 2 == 1:
                return array[len(array)//2]
            else:
                return (array[len(array)//2] + array[len(array)//2 - 1]) / 2
        
        
        rt = []
        for i in range(k,len(nums)+1):
            subArray = nums[i-k:i]
            rt.append(median(subArray))
        return rt
        