class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left= 0 ; right = len(tokens) - 1
        score = 0 ; ans = 0
        while left <= right:
            if tokens[left] <= power:
                power -= tokens[left]
                score += 1
                left += 1
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
            # print(score,power,ans)
            ans = max(ans,score)
        return ans
        