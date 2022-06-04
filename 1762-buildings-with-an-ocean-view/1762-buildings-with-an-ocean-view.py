class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxHeight = 0
        ans = []
        for i in range(len(heights) - 1 , -1, -1):
            if heights[i] > maxHeight:
                ans.insert(0,i)
                maxHeight = heights[i]
        return ans
                
        