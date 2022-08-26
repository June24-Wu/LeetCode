class Solution:

    def __init__(self, nums: List[int]):
        self.table = collections.defaultdict(list)
        for idx , item in enumerate(nums):
            self.table[item].append(idx)
        
    def pick(self, target: int) -> int:
        return self.table[target][random.randint(0,len(self.table[target]) - 1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)