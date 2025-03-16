class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or i == k or j == k:
                        continue
                    num = digits[i]*100 + digits[j] * 10 + digits[k]
                    if num % 2 == 0 and len(str(num)) == 3:
                        ans.add(num)
        # print(ans)
        return len(ans)
        