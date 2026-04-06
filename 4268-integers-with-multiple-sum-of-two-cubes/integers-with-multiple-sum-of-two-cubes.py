class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        m = collections.defaultdict(int)

        for i in range(1000):
            for j in range(i,1000):
                m[i*i*i + j*j*j] += 1
                if i*i*i + j*j*j > n:
                    break
            if i*i*i > n:
                break
                # if i == 9 and j == 15:
                #     print(i*i*i + j*j*j,m[4104])
                # if i == 2 and j == 16:
                #     print(i*i*i + j*j*j,m[4104])
        ans = []
        for i in m:
            if m[i] > 1 and i <= n:
                ans.append(i)
        # for i in vis:
        #     if n - i in vis:
        #         return []
        return sorted(ans)
        