class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        table1 = {i:idx for idx,i in enumerate(nums1)}
        table2 = {i:idx for idx,i in enumerate(nums2)}
        @cache
        def dfs(num,index):
            if num == 1 and index == len(nums1):
                return 0
            if num == 2 and index == len(nums2):
                return 0
            if num == 1 and nums1[index] in table2:
                return nums1[index] + max(dfs(1,index+1),dfs(2,table2[nums1[index]] + 1))
            if num == 2 and nums2[index] in table1:
                return nums2[index] + max(dfs(2,index+1),dfs(1,table1[nums2[index]] + 1))   
            return nums1[index] + dfs(num,index+1) if num == 1 else nums2[index] + dfs(num,index+1)
        return max(dfs(1,0),dfs(2,0)) % (10**9 + 7)
        