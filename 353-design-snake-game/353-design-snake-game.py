class SnakeGame:

    def __init__(self, w: int, h: int, food: List[List[int]]):
        self.body = [(0,0)]
        self.w = w
        self.h = h
        self.food = food
        self.length = 0

    def move(self, direction: str) -> int:
        r , c = self.body[-1]
        if direction == "U":
            r -= 1
        elif direction == "L":
            c -= 1
        elif direction == "R":
            c += 1
        elif direction == "D":
            r += 1
        if self.food and [r,c] == self.food[0]:
            self.food.pop(0)
            self.length += 1
        else:
            self.body.pop(0)
        curr = (r,c)
        if curr in self.body or r >= self.h or r < 0 or c < 0 or c >= self.w:
            return - 1
        self.body.append(curr)
        return self.length
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)