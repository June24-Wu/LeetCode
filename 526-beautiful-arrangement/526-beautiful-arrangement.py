class Solution:
    def countArrangement(self, n: int) -> int:
        visited = set()
        ans = 0
        def backtracking(index):
            nonlocal ans
            if index > n:
                ans += 1
                return
            for i in range(1,n+1):
                if i not in visited and (i % index == 0 or index % i == 0):
                    visited.add(i)
                    backtracking(index + 1)
                    visited.remove(i)
            return
        backtracking(1)
        return ans
        