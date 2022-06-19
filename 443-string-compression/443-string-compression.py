class Solution:
    def compress(self, chars: List[str]) -> int:
        p1 = 0
        while p1 < len(chars):
            p2 = p1 + 1
            length = 1
            while p2 < len(chars) and chars[p1] == chars[p2]:
                chars.pop(p2)
                length += 1
            if length > 1:
                for i in str(length):
                    chars.insert(p2,i)
                    p2 += 1
            p1 = p2
        return len(chars)
                
        