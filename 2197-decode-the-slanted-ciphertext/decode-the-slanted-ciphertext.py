class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows

        li = [[None for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                li[i][j] = encodedText[i * cols + j]
        
        ans = []
        for j in range(cols):
            for i in range(rows):
                if i + j >= cols:
                    break
                ans.append(li[i][i+j])
        # print(ans)

        return "".join(ans).rstrip()
        