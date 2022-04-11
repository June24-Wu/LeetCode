class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        new_arr = []
        for i in range(m):
            new_arr.append(original[i*n:(i+1)*n])
        return new_arr
            
        