class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        table = {num : arr.count(num) for num in set(arr)}
        nums = sorted(list(table.keys()))
        cnt = 0
        for i in nums:
            for j in nums:
                k = target - i - j
                if k not in table:
                    continue
                cntI  = table[i] ; cntJ = table[j] ; cntK = table[k]
                if i == j == k:
                    if cntI <= 2:
                        continue
                    else:
                        cnt += (cntI - 2) * (cntJ-1) * cntK / 6
                elif i == j:
                    cnt += (cntI) * (cntJ-1) / 2 * cntK
                elif i < j < k:
                    cnt += cntI * cntJ * cntK
        return int(cnt % (1e9+7))
        