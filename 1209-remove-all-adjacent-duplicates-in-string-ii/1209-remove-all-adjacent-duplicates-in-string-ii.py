class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        cnt = 0 ; pre = None
        for item in s:
            if stack and stack[-1][0] == item:
                cnt = stack[-1][1] + 1
            else:
                cnt = 1
            stack.append((item,cnt))
            if cnt == k:
                for _ in range(k):
                    stack.pop()
        print(stack)
        return "".join([i[0] for i in stack])