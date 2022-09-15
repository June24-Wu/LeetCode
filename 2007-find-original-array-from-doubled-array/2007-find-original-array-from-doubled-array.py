class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        table = Counter(changed)
        keys = list(table.keys())
        keys.sort()
        ans = []
        print(table)
        for i in keys:
            if table[i] == 0:
                continue
            if table[i] <= table[i*2]:
                if i == 0:
                    if table[i] % 2 != 0:
                        return []
                    for _ in range(table[i] // 2):
                        ans.append(i)
                    continue
                for _ in range(table[i]):
                    ans.append(i)
                table[i*2] -= table[i]
                table[i] -= table[i]
            else:
                return []
        # print(table)
        return ans