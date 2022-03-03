class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # p1 = 0
        # p2 = 0
        # output = [0 for _ in range(len(temperatures))]
        # while p1 < len(temperatures):
        #     p2 = p2 + 1
        #     if p2 >= len(temperatures):
        #         p1 += 1
        #         p2 = p1
        #     elif temperatures[p2] > temperatures[p1]:
        #         output[p1] = p2-p1
        #         p1 += 1
        #         p2 = p1
        # return output
        length = len(temperatures)
        output = [0 for _ in range(length)]
        stack = []
        for i in range(length):
            temperature = temperatures[i]
            while stack != [] and temperature > temperatures[stack[-1]]:
                val = stack.pop()
                output[val] = i - val
            stack.append(i)
        return output
            
        
            
        