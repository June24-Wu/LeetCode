class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        arr = [0 for _ in range(n**2+1)]
        for i in grid:
            for j in i:
                arr[j] += 1
        for i in range(1,len(arr)):
            if arr[i] == 2:
                missing = i
            if arr[i] == 0:
                repete = i
        return [missing,repete]
        