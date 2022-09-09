class Solution:
    def numberOfWeakCharacters(self, mat: List[List[int]]) -> int:
        mat.sort(key = lambda x : ( - x[0], x [1]))
        ans = 0
        left = 0 ; maxdefense = 0
        print(mat)
        for right in range(len(mat)):
            maxdefense = max(maxdefense,mat[right][1])
            if mat[left][0] == mat[right][0]:
                left = right
            if mat[right][1] < maxdefense:
                ans += 1
        return ans
            