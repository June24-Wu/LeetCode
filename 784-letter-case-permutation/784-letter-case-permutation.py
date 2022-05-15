class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        length = len(s)
        s = list(s)
        
        ans = []
        def backtracking(index):
            nonlocal s
            if index == length:
                ans.append("".join(s[:]))
                return
            if s[index].isalpha():
                for i in [s[index].lower(),s[index].upper()]:
                    s[index] = i
                    backtracking(index+1)
            else:
                backtracking(index+1)
        backtracking(0)
        # print(ans)
        return ans
                
        