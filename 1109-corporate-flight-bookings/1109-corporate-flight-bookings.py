class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        diff = [0 for i in range(n)]
        nums = []
        for i in bookings:
            diff[i[0]-1] += i[2]
            if i[1] < len(diff):
                diff[i[1]] -= i[2]
        pre = 0
        for i in diff:
            pre += i
            nums.append(pre)
        return nums
        
        # 暴力解法，超时
        # nums = [0 for i in range(n+1)]
        # for i in bookings:
        #     for j in range(i[0],i[1] + 1):
        #         nums[j] += i[2]
        # nums.pop(0)
        # return nums
        