class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cnta = 0 ; cntb = 0
        for i in range(1,len(colors) - 1):
            if colors[i] == colors[i-1] == colors[i+1] == "A":
                cnta += 1
            if colors[i] == colors[i-1] == colors[i+1] == "B":
                cntb += 1
        return cnta > cntb
        