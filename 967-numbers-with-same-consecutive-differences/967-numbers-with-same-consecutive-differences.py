class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        path = [] ; ans = set()
        def backtracking(num,index):
            nonlocal path ; nonlocal ans
            if index == n:
                ans.add(int("".join([str(i) for i in path[:]])))
                return
            path.append(num)
            for i in range(0,10):
                if num - i == k or i - num == k:
                    backtracking(i,index + 1)
            path.pop()
            return
        for i in range(1,10):
            backtracking(i,0)
        return list(ans)
        