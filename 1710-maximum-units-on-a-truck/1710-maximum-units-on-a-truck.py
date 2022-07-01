class Solution:
    def maximumUnits(self, boxs: List[List[int]], truckSize: int) -> int:
        boxs.sort(key = lambda x : ( - x[1], - x[0]))
        ans = 0 ; cnt = 0
        
        for num , unit in boxs:
            if cnt + num <= truckSize:
                ans += num * unit
            else:
                ans += unit * (truckSize - cnt)
                break
            cnt += num
        return ans