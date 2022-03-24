class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return_li = []
        def backtracking(start_num,path):
            if len(path) == k:
                if sum(path) == n:
                    return_li.append(path[:])
                return
            for i in range(start_num,10):
                path.append(i)
                backtracking(i+1,path)
                path.pop()
        backtracking(1,[])
        return return_li
        