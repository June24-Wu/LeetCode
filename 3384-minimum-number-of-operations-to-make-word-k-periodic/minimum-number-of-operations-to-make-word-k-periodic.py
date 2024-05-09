class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        m = collections.defaultdict(int)
        for i in range(0,len(word),k):
            m[word[i:i+k]] += 1
        v = max([i for k , i in m.items()])
        return len(word) // k - v
        