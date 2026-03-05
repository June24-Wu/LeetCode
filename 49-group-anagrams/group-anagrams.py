class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for i in strs:
            key = [0 for _ in range(26)]
            for j in i:
                key[ord(j) - ord("a")] += 1
            key = sum([v * 1001**k for k, v in enumerate(key)])
            ans[key].append(i)
            # print(key)
        # print(ans)
        return list(ans.values())
        