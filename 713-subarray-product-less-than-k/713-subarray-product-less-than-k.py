class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0 
        p1 = 0 ; p2 = 0
        cnt = 0
        product = 1
        for p2 in range(len(nums)):
            product = product * nums[p2]
            while product >= k:
                product /= nums[p1]
                p1 += 1
            cnt += p2 - p1 + 1
        return cnt
            
        