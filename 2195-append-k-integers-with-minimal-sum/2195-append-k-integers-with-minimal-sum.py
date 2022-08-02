class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort() ; res = set()
        for i in nums:
            if i <= k + len(res):
                res.add(i)
        total = len(res) + k
        return (1 + total) * total // 2 - sum(res)
                
        