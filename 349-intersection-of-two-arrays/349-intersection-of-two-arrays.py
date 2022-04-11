class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums1.sort() ; nums2.sort()
        
        rt = []
        for i in nums2:
            if i in nums1:
                rt.append(i)
        return rt
                