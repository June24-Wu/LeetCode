class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        left = [0] * len(dominoes)
        right = [0] * len(dominoes)
        
        curr = 0
        for i in range(len(dominoes)):
            if dominoes[i] == "R":
                curr = 1
                right[i] = curr
                continue
            if dominoes[i] !="L" and curr > 0:
                curr += 1
                right[i] = curr
            if dominoes[i] == "L":
                curr = 0
                continue
        curr = 0
        for i in range(len(dominoes)-1,-1,-1):
            if dominoes[i] == "L":
                curr = 1
                left[i] = curr
                continue
            if dominoes[i] !="R" and curr > 0:
                curr += 1
                left[i] = curr
            if dominoes[i] == "R":
                curr = 0
                continue
        ans = []
        for i in range(len(dominoes)):
            # print(dominoes[i],left[i],right[i])
            if left[i] == right[i]:
                ans.append('.')
            elif right[i] == 0:
                ans.append("L")
            elif left[i] == 0:
                ans.append("R")
            else:
                ans.append("R" if left[i]>right[i] else "L")
        return "".join(ans)

                
        