class Solution:
    # import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for i in nums:
            if i not in table.keys():
                table[i] = 0
            table[i] += 1
        arr = []
        for i in table.keys():
            arr.append([i,table[i]])
        arr.sort(key = lambda x:(-x[1]))
        rt = []
        
        for i in range(k):
            rt.append(arr[i][0])
        # print(arr)
        return rt
            
        