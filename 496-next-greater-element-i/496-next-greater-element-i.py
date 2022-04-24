class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        
        li2 = [0 for _ in range(len(nums2))]
        res = []
        for i in range(len(nums2)-1,-1,-1):
            while stack != [] and nums2[i] >= stack[-1]:
                stack.pop()
            li2[i] = -1 if stack == [] else stack[-1]
            stack.append(nums2[i])
        for i in nums1:
            res.append(li2[nums2.index(i)])
        return res
        