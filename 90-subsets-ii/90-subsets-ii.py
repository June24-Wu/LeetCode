class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return_li = [[]]
        nums.sort()
        length = len(nums)
        def backtracking(start_index,path):
            if start_index == length:
                return
            for i in range(start_index,length):
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                return_li.append(path[:])
                backtracking(i+1,path)
                path.pop()
        backtracking(0,[])
        return return_li
            
    
#         nums.sort()
#         q = [[]]
#         length = len(nums)
#         for i in nums:
#             for j in range(len(q)):
#                 q.append(q[j] + [i])
        
#         l2 = []
#         for i in q:
#             i = str(i).replace("[","").replace("]","")
#             l2.append(i)
#         l2 = list(set(l2))
#         l3 = []
#         for i in l2:
#             l3.append(i.split(","))
#         return l3
