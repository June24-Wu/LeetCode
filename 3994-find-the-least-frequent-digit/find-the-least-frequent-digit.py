class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        counter = [(v,k) for k, v in Counter(list(str(n))).items()]
        counter.sort()
        return int(counter[0][1])
        
        