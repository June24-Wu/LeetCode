class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_sum = curr_sum = sum(cardPoints[:k])
        for i in range(1,1+k):
            curr_sum += cardPoints[-i] - cardPoints[k-i]
            max_sum = max(max_sum,curr_sum)
        return max_sum
        
        
        
            
        