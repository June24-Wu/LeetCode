class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort()
#         pre = None
#         return_li = {}
#         length = len(candidates)
#         def backtracking(start_index,path):
#             if sum(path) + sum(candidates[start_index:]) < target:return
#             if sum(path) == target:
#                 path.sort()
#                 if str(path[:]) in return_li.keys():return
#                 else:
#                     return_li[str(path[:])] = 1
#                 return
#             elif sum(path) > target:
#                 return
#             for i in range(start_index,length):
#                 path.append(candidates[i])
#                 backtracking(i+1,path)
#                 path.pop()
#         backtracking(0,[])
        
#         table = []
#         for i in return_li.keys():
#             small_table = []
#             i = i.replace("[","")
#             i = i.replace("]","")
#             i = i.split(",")
#             print(i)
#             for j in i:
#                 small_table.append(int(j))
#             table.append(small_table)
#         return table
        candidates.sort()
        return_li = []
        length = len(candidates)
        def backtracking(start_index,path,target):
            if target == 0:
                path.sort()
                return_li.append(path[:])
            for i in range(start_index,length):
                if (i > start_index and candidates[i] == candidates[i-1]):
                    continue
                if (candidates[i] > target):
                    return
                path.append(candidates[i])
                backtracking(i+1,path,target - candidates[i])
                path.pop()
        backtracking(0,[],target)
    
        return return_li