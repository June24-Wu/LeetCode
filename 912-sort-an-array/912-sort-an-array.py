class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        # Merge Sort
        def sort(l,r):
            if l >= r: return
            mid = (l+r) // 2
            sort(l,mid)
            sort(mid+1,r)
            
            left_arr = nums[l:mid+1]
            right_arr = nums[mid+1:r+1]
            arr = []
            
            p1 = 0; p2 = 0
            
            while p1 < len(left_arr) and p2 < len(right_arr):
                if left_arr[p1] <= right_arr[p2]:
                    arr.append(left_arr[p1])
                    p1 += 1
                else:
                    arr.append(right_arr[p2])
                    p2 += 1
            if p1 >= len(left_arr):
                for i in range(p2,len(right_arr)):
                    arr.append(right_arr[i])
            else:
                for i in range(p1,len(left_arr)):
                    arr.append(left_arr[i])
            nums[l:r+1] = arr[:]
            return 
        sort(0,len(nums)-1)
        return nums
            
            
        
        
        # Quick Sort
        
#         def sort(left,right):
#             mid = random.randint(left,right)
#             mid_num = nums[mid]
#             nums[mid] , nums[right] = nums[right] , nums[mid]
            
#             p = left
            
#             for i in range(left,right):
#                 if nums[i] < mid_num:
#                     nums[i] , nums[p] = nums[p] , nums[i]
#                     p += 1
            
#             nums[p] , nums[right] =  nums[right] , nums[p]
#             return p
        
#         def sort2(l,r):
#             if l >= r:return
#             mid = sort(l,r)
#             sort2(mid+1,r)
#             sort2(l,mid-1)
        
#         sort2(0,len(nums)-1)
        
#         return nums
            
        