class Solution:
    def minDeletions(self, s: str) -> int:
        table = collections.defaultdict(int)
        for char in set(list(s)):
            cnt = s.count(char)
            table[cnt] += 1
        rm = 0
        keys = list(table.keys())
        keys.sort()
        # print(table)
        while keys:
            cnt = keys.pop()
            if table[cnt] == 1:
                continue
            if cnt - 1 not in keys and cnt - 1 > 0:
                keys.append(cnt - 1)
            rm += table[cnt] - 1
            table[cnt - 1] += table[cnt] - 1
            # print(keys,rm)
        return rm
                
        