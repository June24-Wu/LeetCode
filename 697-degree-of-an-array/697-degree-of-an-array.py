class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        table = {}
        for i in range(len(nums)):
            if nums[i] not in table.keys():
                table[nums[i]] = [1] + [None for i in range(2)]
                table[nums[i]][1] = i
            else:
                table[nums[i]][0] += 1
                table[nums[i]][2] = i
                
        
        max_val = 0
        for i in table.keys():
            if table[i][0] > max_val:
                max_val = table[i][0]
                left_index = table[i][1]
                right_index = table[i][2]
                if right_index == None:
                    final = 1
                else:
                    final = right_index - left_index + 1
            elif table[i][0] == max_val:
                left_index = table[i][1]
                right_index = table[i][2]
                if right_index == None:
                    final = min(final,1)
                else:
                    final = min(final,table[i][2] -table[i][1] + 1)
                
                
        return final
            
                
                
                
        