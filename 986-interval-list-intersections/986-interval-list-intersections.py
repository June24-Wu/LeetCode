class Solution:
    def intervalIntersection(self, l1: List[List[int]], l2: List[List[int]]) -> List[List[int]]:
        arr = []
        for s , e in l1:
            arr.append((s,1))
            arr.append((e,-1))
        for s , e in l2:
            arr.append((s,1))
            arr.append((e,-1)) 
        arr.sort(key = lambda x : (x[0], - x[1]))
        flag = False ; cnt = 0 ; left = 0 ; ans = []
        for idx , val in arr:
            cnt += val
            if flag == False and cnt == 2:
                left = idx
                flag = True
            if flag and cnt < 2:
                ans.append([left,idx])
                flag = False
        return ans