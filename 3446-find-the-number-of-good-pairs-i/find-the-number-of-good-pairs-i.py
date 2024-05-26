class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        m = len(nums1) ; n = len(nums2)
        for i in range(m):
            for j in range(n):
                if nums1[i] % (nums2[j] * k) == 0:
                    ans += 1
                    # print(i,j)
        return ans
        