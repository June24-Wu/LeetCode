class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = [0 for _ in range(n)]
        original_ratings = ratings.copy()
        ratings = [[i, ratings[i]] for i in range(n)]
        
        ratings.sort(key = lambda x : (x[1],-x[0]))
        for i in range(n):
            candy = 1
            idx , rating = ratings[i]
            if idx - 1 >= 0 and original_ratings[idx] > original_ratings[idx-1]:
                candy = max(candy,ans[idx-1] + 1)
            if idx + 1 < n and original_ratings[idx] > original_ratings[idx+1]:
                candy = max(candy,ans[idx+1] + 1)
            ans[idx] = candy
        # print(ans)
        return sum(ans)