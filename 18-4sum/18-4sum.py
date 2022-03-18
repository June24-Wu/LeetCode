class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        return_li = []
        for first_index in range(len(nums)):
            # if nums[first_index] > target:
            #     break
            if first_index > 0 and nums[first_index] == nums[first_index-1]:
                continue
            for second_index in range(first_index+1,len(nums)):
                left = second_index + 1
                right = len(nums) - 1
                # if nums[first_index] + nums[second_index] > target:
                #     break
                if second_index > first_index+1 and nums[second_index] == nums[second_index-1]:
                    continue
                while left < right:
                    sum_val = nums[first_index] + nums[second_index] + nums[left] + nums[right]
                    if sum_val > target:
                        right -= 1
                    elif sum_val < target:
                        left += 1
                    else:
                        return_li.append([nums[first_index], nums[second_index],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]:left+=1
                        while left < right and nums[right] == nums[right-1]:right-=1
                        left += 1
                        right -= 1
        return return_li