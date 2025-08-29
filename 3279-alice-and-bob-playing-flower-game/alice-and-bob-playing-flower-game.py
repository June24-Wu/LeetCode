class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        even_n = n // 2
        odd_n = n - n // 2

        even_m = m // 2
        odd_m = m - even_m

        return even_n * odd_m + odd_n * even_m
        