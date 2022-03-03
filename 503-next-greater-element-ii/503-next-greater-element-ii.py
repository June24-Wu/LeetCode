class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        stack = []
        output = [-1 for _ in range(length)]
        for i in range(length * 2 - 1):
            num = nums[i %length] # 2
            while stack != [] and num > nums[stack[-1]]:
                index = stack.pop()
                output[index] = nums[i % length]
            stack.append(i % length)
        return output
    
    
#         n = len(nums)
#         ret = [-1] * n
#         stk = list()

#         for i in range(n * 2 - 1):
#             while stk and nums[stk[-1]] < nums[i % n]:
#                 ret[stk.pop()] = nums[i % n]
#             stk.append(i % n)
        
#         return ret