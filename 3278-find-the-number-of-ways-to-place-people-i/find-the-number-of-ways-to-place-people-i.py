class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                left = points[i]
                right = points[j]
                if left[0] <= right[0] and left[1] >= right[1]:
                    is_valid = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        if not is_valid:
                            continue
                        middle = points[k]
                        if left[0] <= middle[0] <= right[0] and right[1] <= middle[1] <= left[1]:
                            is_valid = False
                            break
                    if is_valid:
                        ans += 1
        return ans
        