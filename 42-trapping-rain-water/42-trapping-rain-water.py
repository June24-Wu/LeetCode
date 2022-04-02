class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        leftHeight, rightHeight = [ 0 for _ in range(len(height))] , [ 0 for _ in range(len(height))]
        
        for i in range(0,len(height)-1):
            leftHeight[i+1] = max(leftHeight[i],height[i])
        print(leftHeight)
        
        for i in range(len(height)-1,0,-1):
            rightHeight[i-1] = max(rightHeight[i],height[i])
        print(rightHeight)
        for i in range(1,len(height)-1):
            area += min(leftHeight[i],rightHeight[i]) - height[i] if min(leftHeight[i],rightHeight[i]) - height[i] > 0 else 0
        return area
        
        