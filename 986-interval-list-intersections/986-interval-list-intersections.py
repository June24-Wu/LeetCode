class Solution:
    def intervalIntersection(self, l1: List[List[int]], l2: List[List[int]]) -> List[List[int]]:
        array = []
        for start , end in l1:
            array.append((start,1))
            array.append((end,-1))
        for start , end in l2:
            array.append((start,1))
            array.append((end,-1))
        array.sort(key = lambda x : (x[0], - x[1]))
        flag = False
        cnt = 0
        ans = []
        for start , num in array:
            cnt += num
            if flag == False and cnt == 2:
                left = start
                flag = True
            if flag == True and cnt < 2:
                ans.append([left, start])
                flag = False
        return ans