class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        nums = [str(i) for i in nums]
        ans = 0
        table = set()
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                cnt = 0
                for t in nums[i:j+1]:
                    if int(t) % p == 0:
                        cnt += 1
                if cnt <= k and ",".join(nums[i:j+1]) not in table:
                    table.add(",".join(nums[i:j+1]))
                    # print(nums[i:j+1])
                    
                    ans += 1
        return ans
        