class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        arr = []
        for left , right , val in buildings:
            arr.append((left,val))
            arr.append((right,-val))
        arr.sort(key = lambda x : (x[0],-x[1]))
        # print(arr)
        
        ans = [] ; heights = [] ; leftH = 0
        
        for idx , h in arr:
            if heights == []:
                heights.append(-h)
                ans.append([idx,h])
                leftH = h
                continue
            maxVal = - heights[0]
            if h > 0:
                if h > maxVal:
                    ans.append([idx,h])
                    leftH = h
                heights.append(-h)
            else:
                h = abs(h)
                if h >= maxVal:
                    heapq.heappop(heights)
                    currH = - heights[0] if len(heights) > 0 else 0
                    if currH != leftH:
                        ans.append([idx,currH])
                        leftH = currH
                else:
                    heights.pop(heights.index(-h))
            heapq.heapify(heights)
            # print(heights)
        return ans
                
                    
        