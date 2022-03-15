class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        li = [i+1 for i in range(n)]
        minVal = n-k+1
        maxVal = n
        flag = 0
        for i in range(n-k,n):
            if flag ==1:
                li[i] = minVal
                minVal += 1
                flag = 0
            else:
                li[i] = maxVal
                maxVal -= 1
                flag = 1
        return li
            
            
            
        