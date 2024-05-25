class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict) ; ans = []
        def bt(left,right,curr):
            nonlocal ans
            # print(left,right,curr)
            if right == len(s):
                if s[left:] in wordDict:
                    ans.append(curr + [s[left:right+1]])
                return
            if s[left:right+1] in wordDict:
                bt(right+1,right+1,curr + [s[left:right+1]])
            bt(left,right+1,curr)
            return
        bt(0,0,[])
        return [" ".join(i) for i in ans]
            

        