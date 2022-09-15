class Solution:
    def maxProduct(self, words: List[str]) -> int:
        table = collections.defaultdict(set)
        for word in words:
            for i in word:
                table[word].add(i)
        keys = list(table.keys())
        ans = 0
        for i in range(len(keys)):
            for j in range(i+1,len(keys)):
                flag = True
                for char in table[keys[i]]:
                    if char in table[keys[j]]:
                        flag = False
                        break
                if flag:
                    ans = max(len(keys[i]) * len(keys[j]),ans)
        return ans
        