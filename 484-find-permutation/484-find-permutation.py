class Solution:
    def findPermutation(self, s: str) -> List[int]:
        curr = 1
        stack = []
        ans = []
        for char in s:
            stack.append(curr)
            curr += 1
            if char == "I":
                while stack:
                    ans.append(stack.pop())
            else:
                continue
        stack.append(curr)
        while stack:
            ans.append(stack.pop())
        return ans
        