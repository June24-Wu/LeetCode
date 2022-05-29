class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [int(i) for i in list(str(num))]
        table = {}
        for index, item in enumerate(nums):
            table[item] = index
        for index, item in enumerate(nums):
            for j in range(9,item,-1):
                if j in table and table[j] > index:
                    nums[table[j]] , nums[index] =  nums[index] , nums[table[j]]
                    nums = [str(i) for i in nums]
                    return int("".join(nums))
        nums = [str(i) for i in nums]
        return int("".join(nums))