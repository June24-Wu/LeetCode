class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        m = collections.defaultdict(int)

        single = 0
        for word in words:
            if len(word) < k:
                # single += 1
                continue
            prefix = word[:k]
            m[prefix] += 1

        ans = 0
        for k, v in m.items():
            if v > 1:
                ans += 1
            elif v == 1 and single > 0:
                ans += 1
                single -= 1
        return ans
            # m[prefix/] = m.get(prefix,[])
            # m[prefix].append(word)
        