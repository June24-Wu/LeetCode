class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums))] ; postfix = [1 for _ in range(len(nums))]
        
        val = 1 
        for i in range(len(nums)):
            val = val * nums[i]
            prefix[i] = val
        val = 1
        for i in range(len(nums)-1,-1,-1):
            val = val *nums[i]
            postfix[i] = val
        
        ans = []
        def get(array,index):
            if index < 0 or index >= len(array):
                return 1
            return array[index]
        for i in range(len(nums)):
            val = get(prefix,i-1)
            val *= get(postfix,i+1)
            ans.append(val)
        # print(prefix)
        # print(postfix)
        return ans
            