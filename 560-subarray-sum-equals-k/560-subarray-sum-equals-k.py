class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       
        cnt = 0
        
        table = {0:1}
        pre = 0
        for i in range(len(nums)):
            pre = pre + nums[i]
            if pre - k in table.keys():
                cnt += table[pre - k]
            table[pre] = 1 if pre not in table.keys() else  table[pre] + 1

        print(table)
        return cnt
        