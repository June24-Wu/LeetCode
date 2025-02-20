class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums[0])
        for i in range(2**17):
            i = bin(i)[2:]
            while len(i) < length:
                i = "0" + i
            if i not in nums:
                return i
        # return ""
        