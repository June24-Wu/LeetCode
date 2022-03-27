class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        res = []
        for i in range(len(gas)):
            res.append(gas[i]-cost[i])
            
        if sum(res) < 0:return -1
        
        
        sumVal = 0
        start_index = 0
        
        for i in range(len(res)):
            sumVal += res[i]
            if sumVal < 0:
                start_index = i + 1
                sumVal = 0
        return start_index