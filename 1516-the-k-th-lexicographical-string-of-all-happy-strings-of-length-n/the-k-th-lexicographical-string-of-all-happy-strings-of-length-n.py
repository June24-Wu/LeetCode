class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        curr = []
        def bt(idx):
            nonlocal curr
            nonlocal ans
            if len(ans) == k:
                return
            if idx == n:
                ans.append("".join(curr))
                return
            for i in ["a","b","c"]:
                if curr and curr[-1] == i:
                    continue
                curr.append(i)
                bt(idx+1)
                curr.pop()
            return
        bt(0)
        return ans[-1] if len(ans) == k else ""