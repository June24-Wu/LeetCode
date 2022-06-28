"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        table = []
        for employee in schedule:
            for time in employee:
                s , e = time.start , time.end
                table.append((s,1))
                table.append((e,-1))
        table.sort()
        cnt = 0 ; flag = False ; ans = [] ; s = None
        for idx , item in table:
            cnt += item
            if cnt == 0 and flag:
                s = idx
                flag = False
            if cnt > 0 and not flag:
                if s != None and idx - s > 0:
                    ans.append(Interval(start = s , end = idx))
                s = None
                flag = True
        return ans
                
        