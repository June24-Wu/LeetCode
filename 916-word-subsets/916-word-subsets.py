class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        table = collections.defaultdict(int)
        
        for word in words2:
            subtable = collections.defaultdict(int)
            for i in word:
                subtable[i] += 1
                table[i] = max(table[i],subtable[i])
        ans = []
        
        for word in words1:
            flag = True
            subtable = collections.defaultdict(int)
            for i in word:
                subtable[i] += 1
            for i in table:
                if table[i] > subtable[i]:
                    flag = False
                    break
            if flag:
                ans.append(word)
        return ans
                