class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0 ; y = 0
        for i in moves:
            if i == "U":
                x += 1
            elif i == "D":
                x -= 1
            elif i == "L":
                y -= 1
            else:
                y += 1
        return x == 0 and y == 0