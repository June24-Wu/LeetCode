class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return_li = [0 for _ in range(len(temperatures))]
        
        stack = []
        
        for i in range(len(temperatures)):
            if stack == []:
                stack.append(i)
            else:
                while stack != []:
                    last = stack.pop()
                    if temperatures[i] > temperatures[last]:
                        return_li[last] = i - last
                    else:
                        stack.append(last)
                        break
                stack.append(i)
        return return_li
            
        
            
        