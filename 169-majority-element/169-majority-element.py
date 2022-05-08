class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # length = len(nums) / 2
        # table = {}
        # for i in nums:
        #     if i not in table:
        #         table[i] = 0
        #     table[i] += 1
        # for i in table:
        #     if table[i] >= length:
        #         return i
        
        
        # 分治
        def divide(left,right):
            if left == right:
                return nums[left]
            mid = (left+right) // 2
            left_majority = divide(left,mid)
            right_majority = divide(mid+1,right)
            if left_majority == right_majority:
                return left_majority
            left_majority_cnt = sum(1 for i in nums[left:mid+1] if i == left_majority)
            right_majority_cnt = sum(1 for i in nums[mid+1:right+1] if i == right_majority)
            if left_majority_cnt > right_majority_cnt:
                return left_majority
            else:
                return right_majority
        return divide(0,len(nums)-1)
        