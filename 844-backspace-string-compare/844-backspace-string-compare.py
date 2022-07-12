class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = []
        for i in s:
            if i != "#":
                a.append(i)
            else:
                if a:
                    a.pop()
        b = []
        for i in t:
            if i != "#":
                b.append(i)
            else:
                if b:
                    b.pop()
        return a == b
                
        