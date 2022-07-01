class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        visited = set() # (0,0,"E")
        
        def l(location):
            x , y , face = location
            if face == "E":
                face = "N"
            elif face == "N":
                face = "W"
            elif face == "W":
                face = "S"
            elif face == "S":
                face = "E"
            return (x , y ,face)
        def r(location):
            x , y , face = location
            if face == "E":
                face = "S"
            elif face == "N":
                face = "E"
            elif face == "W":
                face = "N"
            elif face == "S":
                face = "W"
            return (x , y ,face)
        def g(location):
            x , y , face = location
            if face == "E":
                x += 1
            elif face == "W":
                x -= 1
            elif face == "N":
                y += 1
            elif face =="S":
                y -= 1
            return (x,y,face)
        curr = (0,0,"E")
        for _ in range(100):
            for i in instructions:
                if i == "G":
                    curr = g(curr)
                elif i == "L":
                    curr  = l(curr)
                elif i == "R":
                    curr = r(curr)
            if curr == (0,0,"E"):
                return True
        return False
        
        