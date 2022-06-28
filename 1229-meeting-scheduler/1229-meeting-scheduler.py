class Solution:
    def minAvailableDuration(self, s1: List[List[int]], s2: List[List[int]], duration: int) -> List[int]:
        arr = []
        for s , e in s1:
            arr.append((s,1))
            arr.append((e, - 1))
        for s , e in s2:
            arr.append((s,1))
            arr.append((e, - 1))
        arr.sort()
        
        flag = False ; left = 0 ; cnt = 0
        for idx , val in arr:
            cnt += val
            if not flag and cnt == 2:
                flag = True
                left = idx
            if flag and cnt < 2:
                flag = False
                if idx - left >= duration:
                    return [left,left + duration]
        return []
        