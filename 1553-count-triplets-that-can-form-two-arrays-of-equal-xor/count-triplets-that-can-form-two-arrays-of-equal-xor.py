class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0

        xor = [0] * len(arr)
        xor[0] = arr[0]

        seen = defaultdict(list)
        seen[xor[0]].append(0)
        seen[0].append(-1)

        for i in range(1, len(arr)):
            xor[i] = xor[i-1] ^ arr[i]
            for l in seen[xor[i]]:
                ans += i-l-1
            seen[xor[i]].append(i)
        return ans