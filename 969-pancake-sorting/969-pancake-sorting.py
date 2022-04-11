class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        
        def flip(p1,p2):
            while p1 <= p2:
                arr[p1] , arr[p2] = arr[p2] , arr[p1]
                p1 += 1
                p2 -= 1
            
        def twoflips(index,length):
            flip(0,index)
            flip(0,length)
            

        rt = []
        for i in range(len(arr)-1,0,-1):
            indexOfMax = arr[:i].index(max(arr[:i]))
            if arr[indexOfMax] < arr[i]:
                continue
            rt.append(indexOfMax+1)
            rt.append(i+1)
            twoflips(indexOfMax,i)
        return rt
        