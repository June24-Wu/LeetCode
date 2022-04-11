class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort() ; nums2.sort()
        
        p = 0
        rt = []
        for i in nums1:
            if i in nums2:
                rt.append(i)
                nums2.pop(nums2.index(i))
        return rt
        