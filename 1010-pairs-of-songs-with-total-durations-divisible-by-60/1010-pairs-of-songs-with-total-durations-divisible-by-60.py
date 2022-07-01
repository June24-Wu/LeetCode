class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        table = {}
        for i in time:
            i = i % 60
            if i not in table:
                table[i] = 0
            table[i] += 1
        cnt = 0
        visited = set()
        for i in table:
            if i in visited:
                continue
            if i in [30,0]:
                cnt += (table[i] * (table[i] - 1)) // 2
            else:
                res = 60 - i
                if res in table:
                    cnt += table[i] * table[res]
                    visited.add(i)
                    visited.add(res)
        return cnt
        