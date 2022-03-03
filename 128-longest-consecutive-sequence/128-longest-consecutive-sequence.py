class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = {}
        max_value = 0
        for i in nums:
            if i in table.keys():
                continue
            if (i-1) in table.keys():
                left = table[i-1]
            else:
                left = 0
            
            if (i+1) in table.keys():
                right = table[i+1]
            else:
                right = 0
            value = left + right + 1
            table[i] = value
            for j in range(left):
                table[i-j-1] = value
            for j in range(right):
                table[i+j+1] = value           
    
            max_value = value if value > max_value else max_value
        return max_value
        