class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        q = deque([(0, 0, False)])
        visited = set()
        MAX_DIST = max(x, max(forbidden)) + a + b
        while q:
            res, currPos, prevWasBackwards = q.popleft()
            if currPos == x:
                return res
            
            if (currPos + a not in forbidden and
                currPos + a <= MAX_DIST and
                (currPos + a, False) not in visited
               ):
                q.append((res + 1, currPos + a, False))
                visited.add((currPos + a, False))

            if (currPos - b not in forbidden and
                currPos - b >= 0 and
                not prevWasBackwards and
                (currPos - b, prevWasBackwards) not in visited
               ):
                q.append((res + 1, currPos - b, True))
                visited.add((currPos - b, True))                    
        return -1
    # Time: O(n) where n is x
    # Space: O(n) it's the space for the queue