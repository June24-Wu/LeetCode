class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        for i in range(len(nums1)):
            val = nums1[i]
            if val >= max(nums2):
                nums1[i] = -1
            nums1[i] = -1
            for j in range(len(nums2)):
                if val == nums2[j]:
                    for t in range(j+1,len(nums2)):
                        if nums2[t] > val:
                            nums1[i] = nums2[t]
                            break
                    break
        return nums1
        