class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        dp = [0 for _ in range(len(nums1))]
        
        for item in nums2:
            for j in range(len(nums1)-1,-1,-1):
                if nums1[j] == item:
                    if j == 0:
                        dp[j] = 1
                    else:
                        dp[j] = max(dp[:j]) + 1
            # print(dp)
        return max(dp)