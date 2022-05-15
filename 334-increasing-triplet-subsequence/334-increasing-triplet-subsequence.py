class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        leftMaxArray = [0 for i in range(len(nums))] ; rightMaxArray = [0 for i in range(len(nums))] 
        maxVal = float("inf")
        for i in range(len(nums)):
            leftMaxArray[i] = maxVal
            maxVal = min(maxVal,nums[i])
        maxVal = 0
        for i in range(len(nums)-1,-1,-1):
            rightMaxArray[i] = maxVal
            maxVal = max(maxVal,nums[i])
        print(leftMaxArray)
        print(rightMaxArray)
        for i in range(1,len(nums)-1):
            if nums[i] > leftMaxArray[i] and nums[i] < rightMaxArray[i]:
                return True
        return False