class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def calculate():
            nonlocal height
            nonlocal ans
            left = [-1 for i in range(len(height))] ; right = [len(height) for i in range(len(height))]
            stack = []
            for i in range(len(height)):
                while stack != [] and height[i] <= height[stack[-1]]:
                    stack.pop()
                left[i] = stack[-1] if stack != [] else -1
                stack.append(i)
            stack = []
            for i in range(len(height)-1,-1,-1):
                while stack != [] and height[i] <= height[stack[-1]]:
                    stack.pop()
                right[i] = stack[-1] if stack != [] else len(height)
                stack.append(i)

            for index , item in enumerate(height):
                ans = max(ans,(right[index] - left[index] - 1) * item)
        ans = 0
        for i , row in enumerate(matrix):
            if i == 0:
                height = [0 if i == "1" else 1 for i in row]
            for j in range(len(row)):
                if row[j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            calculate()
        # print(ans)
        # print(height)
        return ans

