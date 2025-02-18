class Solution:
    def smallestNumber(self, pattern: str) -> str:
        curr = []
        ans = []
        n = len(pattern)
        def bt(idx):
            nonlocal curr
            nonlocal ans
            if idx == n:
                ans.append("".join([str(k) for k in curr]))
                return
            lastv = curr[-1]
            if pattern[idx] == "I":
                for i in range(lastv+1,10):
                    if i not in curr:
                        curr.append(i)
                        bt(idx+1)
                        curr.pop()
            else:
                for i in range(1,lastv):
                    if i not in curr:
                        curr.append(i)
                        bt(idx+1)
                        curr.pop()
            # print(curr)
            return
        for j in range(1,10):
            curr = [j]
            bt(0)
        ans.sort()
        return ans[0]

        