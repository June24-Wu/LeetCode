class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        unionList = [i for i in range(n)]
        
        def find(index):
            if unionList[index] == index:
                return index
            unionList[index] = find(unionList[index])
            return unionList[index]
        def check(a,b):
            cnt = 0
            for ac , bc in zip(a,b):
                if ac!= bc :
                    cnt += 1
            if cnt > 2:
                return False
            return True
        
        for a in range(n):
            for b in range(a+1,n):
                if find(a) == find(b):
                    continue
                if check(strs[a],strs[b]):
                    unionList[find(b)] = find(a)
        ret = sum(1 for i in range(n) if unionList[i] == i)
        return ret
        
        
        

                    
            
                
        