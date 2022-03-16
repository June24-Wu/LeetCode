class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return_li = []
        length = len(candidates)
        def backtracking(start_index,path):
            if sum(path) == target:
                return_li.append(path[:])
            elif sum(path) > target:
                return
            else:
                for i in range(start_index,length):
                    path.append(candidates[i])
                    backtracking(i,path)
                    path.pop()
        backtracking(0,[])
        return return_li
            
        