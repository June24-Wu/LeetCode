class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        diff = []; n = len(technique1)
        for i in range(n):
            diff.append([i,technique1[i] - technique2[i]])
        diff.sort(key = lambda x : - x[1])
        # print(diff)
        ans = 0
        for i in range(n):
            idx = diff[i][0]
            if i < k or diff[i][1] > 0:
                # print(i < k, diff[idx][1] > 0)
                ans += technique1[idx]
            else:
                ans += technique2[idx]
            # print(i,diff[i],technique1[idx],technique2[idx])
            # print(ans)
        return ans
        