class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left = 0
        curr = 0
        for right in range(minutes):
            if grumpy[right] == 1:
                curr += customers[right]
        ans = curr
        right = minutes
        while right < len(customers):
            if grumpy[left] == 1:
                curr -= customers[left]
            left += 1
            if grumpy[right] == 1:
                curr += customers[right]
            right += 1
            ans = max(curr,ans)
            # print(left,right,curr)
        # print(ans)
        for i in range(len(customers)):
            ans += customers[i] * abs(grumpy[i] - 1)
        return ans 
            
        