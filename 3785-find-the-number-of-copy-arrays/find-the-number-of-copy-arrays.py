class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        minv = bounds[0][0]
        maxv = bounds[0][1]
        # original = [i-original[0] for i in original]
        print(original)
        n = len(original)
        for i in range(1,n):
            diff = original[i] - original[0]
            minv = max(minv,bounds[i][0] - diff)
            maxv = min(maxv,bounds[i][1] - diff)
        return max(maxv - minv + 1,0)
        