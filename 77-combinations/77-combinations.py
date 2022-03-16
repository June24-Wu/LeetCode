class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtracking(start_index,path):
            if len(path) == k:
                return_li.append(path[:])
                return
            for i in range(start_index,n+1):
                path.append(i)
                backtracking(i+1,path)
                path.pop()
            return
        return_li = []
        backtracking(1,[])
        return return_li
    
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         def backtrack(first = 1, curr = []):
#             # if the combination is done
#             if len(curr) == k:  
#                 output.append(curr[:])
#             for i in range(first, n + 1):
#                 # add i into the current combination
#                 curr.append(i)
#                 # use next integers to complete the combination
#                 backtrack(i + 1, curr)
#                 # backtrack
#                 curr.pop()
        
#         output = []
#         backtrack()
#         return output