class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        minVal = float("inf") ; ans = float("inf") ; newNums = []
        for i in nums:
            if i % 2 == 0:
                minVal = min(minVal,i)
                newNums.append(-i)
            else:
                minVal = min(minVal,i*2)
                newNums.append(-i*2)
        heapq.heapify(newNums)
        while newNums:
            curr =  - heapq.heappop(newNums)
            ans = min(ans,abs(curr - minVal))
            if curr % 2 == 0:
                heapq.heappush(newNums,- curr // 2)
                minVal = min(minVal,curr // 2)
            else:
                break
        return ans        