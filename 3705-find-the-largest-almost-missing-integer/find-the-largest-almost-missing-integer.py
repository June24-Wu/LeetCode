class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        m = collections.defaultdict(int)
        n = len(nums)
        for i in range(n-k+1):
            s = set(nums[i:i+k])
            for j in s:
                m[j] += 1
        m = [[v,k] for k,v in m.items()]
        m.sort(key = lambda x : (x[0],-x[1]))
        return m[0][1] if m[0][0] == 1 else -1
        