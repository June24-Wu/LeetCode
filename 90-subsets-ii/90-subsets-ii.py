class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def bt(index,path):
            if index > len(nums):
                return
            ans.append(path[:])
            for i in range(index,len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                bt(i+1,path)
                path.pop()
            return
        bt(0,[])
        return ans
        