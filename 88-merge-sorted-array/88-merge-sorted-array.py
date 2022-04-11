class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        
        p1 = m - 1 ; p2 = n -1
        
        p = m+n - 1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2-=1
            p -= 1
        if p1 < 0:
            for i in range(p2,-1,-1):
                nums1[p] = nums2[i]
                p -= 1
        else:
            for i in range(p1,-1,-1):
                nums1[p] = nums1[i]
                p -= 1
        return nums1
        