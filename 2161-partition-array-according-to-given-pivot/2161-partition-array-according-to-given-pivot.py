class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        nums1 = []; nums2 = [] ; mid = []
        
        for i in nums:
            if i < pivot:
                nums1.append(i)
            elif i == pivot:
                mid.append(i)
            else:
                nums2.append(i)
        nums1.extend(mid)
        nums1.extend(nums2)
        return nums1
        