class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(i) for i in nums]
        nums.sort()
        return str(nums[-k])
#         random.shuffle(nums)
#         def select(left,right,k):
#             p = left
#             for i in range(left,right):
#                 if nums[i] < nums[right]:
#                     nums[p] , nums[i] = nums[i] , nums[p]
#                     p += 1
#             nums[p] , nums[right] = nums[right] , nums[p]
            
#             if right - p == k - 1:
#                 return nums[p]
#             elif right - p > k - 1:
#                 return select(p + 1,right,k)
#             else:
#                 return select(left,p-1,k-1-right+p)
#         return str(select(0,len(nums) - 1 , k))
        