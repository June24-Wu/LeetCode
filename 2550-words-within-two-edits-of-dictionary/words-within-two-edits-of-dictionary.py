class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        def compare(i1,i2):
            diff = 0
            for i in range(len(i1)):
                if i1[i] != i2[i]:
                    diff += 1
                if diff > 2:
                    break
            return diff <= 2
        ans = []
        for word in queries:
            for word2 in dictionary:
                if compare(word,word2):
                    ans.append(word)
                    break
        return ans
                    
                
                    
            
        