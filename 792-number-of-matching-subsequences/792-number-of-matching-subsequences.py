class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        bucket = [[] for _ in range(26)]
        for item in words:
            key = ord(item[0]) - ord("a")
            bucket[key].append(item)
        for i in s:
            key = ord(i[0]) - ord("a")
            old_bucket = bucket[key].copy()
            bucket[key] = []
            while old_bucket:
                item = old_bucket.pop()
                item = item[1:]
                if item == "":
                    continue
                newkey = ord(item[0]) - ord("a")
                bucket[newkey].append(item)
        cnt = len(words)
        for i in bucket:
            cnt -= len(i)
        return cnt
            
                
        