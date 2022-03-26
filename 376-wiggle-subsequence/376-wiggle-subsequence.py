class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 2:return 1
        
        new_li = []
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1] != 0:
                new_li.append(nums[i]-nums[i-1])
        
        
        if len(new_li) == 0: return 1
        bigger = True if new_li[0] > 0 else False
        cnt = 1
        for i in new_li:
            if bigger == True and i > 0:
                cnt += 1
                bigger = False
            if bigger == False and i < 0:
                cnt +=1
                bigger = True
        return cnt
            
            