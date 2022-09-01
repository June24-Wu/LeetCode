class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        heap = []
        table = collections.defaultdict(list)
        for i in range(len(username)):
            heapq.heappush(heap,(timestamp[i],username[i],website[i]))
        while heap:
            time , user , web = heapq.heappop(heap)
            table[user].append(web)
        pattern = collections.defaultdict(int)
        def count(nums):
            nonlocal pattern
            result = set()
            length = len(nums)
            for i in range(length):
                for j in range(i + 1,length):
                    for t in range( j + 1 , length):
                        result.add((nums[i],nums[j],nums[t]))
            for i in result:
                pattern[i] += 1                      
            return
        for i in table:
            count(table[i])
        ans = 0 ; cnt = 0
        for i in pattern:
            if pattern[i] > cnt:
                ans = i
                cnt = pattern[i]
            elif pattern[i] == cnt and  i < ans:
                ans = i
        return ans
                        
        