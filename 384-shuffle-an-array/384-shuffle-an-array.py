from random import shuffle
class Solution:

    def __init__(self, nums: List[int]):
        self.origin = nums
        self.new = nums

    def reset(self) -> List[int]:
        return self.origin
        

    def shuffle(self) -> List[int]:
        self.new = self.origin.copy()
        shuffle(self.new)
        return self.new
                


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()