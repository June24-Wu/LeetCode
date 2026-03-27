class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        m = {}
        vis = set()

        def get_digit_sum(num):
            return sum([int(i) for i in list(str(num))])
        for i in nums:
            digit_sum = get_digit_sum(i)
            if digit_sum in m and digit_sum not in vis:
                m[digit_sum] += i
                vis.add(digit_sum)
            elif digit_sum not in m:
                m[digit_sum] = i
            # print(i,digit_sum,m,vis)

        ans = -1

        for i in vis:
            ans = max(ans,m[i])
        return ans
        