class Solution:
    def maxArea(self, h: int, w: int, hList: List[int], vList: List[int]) -> int:
        hList.sort()
        if hList[0] != 0:
            hList.insert(0,0)
        if hList[-1] != h:
            hList.append(h)
        vList.sort()
        if vList[0] != 0:
            vList.insert(0,0)
        if vList[-1] != w:
            vList.append(w)
        hMax = 0
        for i in range(1,len(hList)):
            hMax = max(hMax,hList[i] - hList[i-1])
        wMax = 0
        for i in range(1,len(vList)):
            wMax = max(wMax,vList[i] - vList[i-1])
        modulo = 10**9 + 7
        return hMax * wMax % modulo