class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        right = m * n - 1
        left = 0
        if m*n == 1:
            if matrix[0][0] == target:
                return True
            else:
                return False
        while right - left > 1:
            mid = (right+left)/2
            mid_val = matrix[int(mid//n)][int(mid%n)]
            if target < mid_val:
                right = mid
            elif target > mid_val:
                left = mid
            else:
                return True
        print(left,right)
        return target == matrix[int(left//n)][int(left%n)] or target == matrix[int(right//n)][int(right%n)] 