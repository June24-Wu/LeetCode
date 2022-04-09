class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        def get(row,column):
            if row == -1 or row == m or column == -1 or column == n:
                return -1
            return mat[row][column]
        
        up,down = 0 , m - 1
        
        while up <= down:
            mid = (up+down) // 2
            maxVal_index = mat[mid].index(max(mat[mid]))
            if get(mid,maxVal_index) > get(mid - 1,maxVal_index) and get(mid,maxVal_index) > get(mid + 1,maxVal_index):
                return ([mid,maxVal_index])
            elif get(mid,maxVal_index) < get(mid + 1,maxVal_index):
                up = mid + 1
            else:
                down = mid - 1
        return ([mid,maxVal_index])        