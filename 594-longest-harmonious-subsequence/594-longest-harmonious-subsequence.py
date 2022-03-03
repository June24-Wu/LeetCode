class Solution:
    def findLHS(self, nums: List[int]) -> int:
        max_value = 0
        table = {}
        for i in nums:
            if i in table.keys():
                table[i] += 1
            else:
                table[i] = 1
            if (i-1) in table.keys():
                value_left = table[i-1]
            else:
                value_left = 0
                
            if (i+1) in table.keys():
                value_right = table[i+1]
            else:
                value_right = 0
            if value_right == 0 and value_left == 0:
                continue
            else:
                value = table[i] + max(value_left,value_right)
            if value > max_value:
                max_value = value
        return max_value
            
            