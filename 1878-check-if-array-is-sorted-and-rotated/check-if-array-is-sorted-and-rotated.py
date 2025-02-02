class Solution:
    def check(self, nums: List[int]) -> bool:
        a = nums[:]
        a.sort()
        def rotate(array):
            n = len(array)
            return [array[(i+1) % n] for i in range(n)] 
        n = len(nums)
        for i in range(2*n):
            a = rotate(a)
            if a == nums:
                return True
        return False
        # return True
        