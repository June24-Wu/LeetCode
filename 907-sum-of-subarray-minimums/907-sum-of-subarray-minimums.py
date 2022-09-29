class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        
        arr.append(0)
        mod = 10**9 + 7
        ans = 0
        stack = [-1]
        for idx2 , item in enumerate(arr):
            while stack and item < arr[stack[-1]]:
                mid = stack.pop()
                left = mid - stack[-1]
                right = idx2 - mid
                print(mid,left,right,arr[mid])
                ans += left * right * arr[mid]
            stack.append(idx2)
        return ans % mod
    
# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
        
#         M = 10**9+7
#         sums = 0
#         arr.append(0) #Sentinel value to pop all elements off the stack
#         stack = [-1]
        
#         for i2,num in enumerate(arr):
# 	      #Mantain a monotone increasing stack
#             while stack and num < arr[stack[-1]]:
#                 index = stack.pop()
#                 i1 = stack[-1]   # First lesser element to the left
#                 left = index-stack[-1]
#                 right = i2-index
#                 sums += right*left*arr[index]
#             stack.append(i2)
            
#         return sums%M
                