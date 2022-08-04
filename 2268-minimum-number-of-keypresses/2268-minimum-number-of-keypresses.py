class Solution:
    def minimumKeypresses(self, s: str) -> int:
        nums = [(s.count(i),i) for i in set(list(s))]
        nums.sort()
        
        cnt = 0
        ans = 0
        print(nums)
        for i in range(len(nums)-1,-1,-1):
            ans += (cnt // 9 + 1) * nums[i][0]
            cnt += 1
        return ans
        