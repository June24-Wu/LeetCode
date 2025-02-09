class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        table = collections.defaultdict(int)
        for index , item in enumerate(nums):
            table[item - index] += 1
        good = sum([table[i] * (table[i]-1) // 2 for i in table])
        n = len(nums)
        return n * (n-1) // 2 - good
        