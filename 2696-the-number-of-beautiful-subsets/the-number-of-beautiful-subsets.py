class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr = [] ; ans = 0
        def dfs(idx):
            nonlocal ans
            if idx == len(nums):
                ans += 1
                return
            if nums[idx] - k not in curr:
                curr.append(nums[idx])
                dfs(idx+1)
                curr.pop()
            dfs(idx+1)
            return
        dfs(0)
        # print(ans)
        return ans - 1


        