class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # method 2 
        final = []
        def backtracking(start_index,path):
            nonlocal final
            if start_index > len(nums):
                return
            final.append(path[:])
            for i in range(start_index,len(nums)):
                path.append(nums[i])
                backtracking(i+1,path)
                path.pop()
        backtracking(0,[])
        return final
        
        # method 1 
        # q=[[]]
        # n=len(nums)
        # for i in range(n):
        #     for j in range(len(q)):
        #         q.append(q[j]+[nums[i]])
        # return q
        