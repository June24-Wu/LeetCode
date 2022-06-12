class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        arr1 = {}
        for i in nums1:
            for j in nums2:
                if (i+j) not in arr1:
                    arr1[i+j] = 0
                arr1[i+j] += 1
        arr2 = {}
        for i in nums3:
            for j in nums4:
                if (i+j) not in arr2:
                    arr2[i+j] = 0
                arr2[i+j] += 1      
        cnt = 0
        for i in arr1:
            if -i in arr2:
                cnt += arr2[-i] * arr1[i]
                del arr2[-i]
        for i in arr2:
            if -i in arr1:
                cnt += arr2[i] * arr1[-i]
        return cnt
        