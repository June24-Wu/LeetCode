
            
        
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        n = len(heights)
        left = [-1 for i in range(n)] ; right = [n for i in range(n)]
        
        for i in range(len(heights)):
            while stack != [] and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack != []:
                left[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(len(heights)-1,-1,-1):
            while stack != [] and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack != []:
                right[i] = stack[-1]
            stack.append(i)
        return max((right[i]-left[i]-1) * heights[i] for i in range(n)) if n > 0 else 0 
