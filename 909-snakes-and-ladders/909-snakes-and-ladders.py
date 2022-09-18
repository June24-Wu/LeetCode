class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get(index):
            div = (index - 1) // n
            mod = (index - 1) % n
            if div % 2 == 0:
                return board[n-div - 1][mod]
            else:
                return board[n-div - 1][n - mod - 1]
        array = [-1 for _ in range(n**2 + 1)]
        for i in range(1,n**2+1):
            array[i] = get(i)
        queue = [(1,0)]
        visited = set()
        while queue:
            curr , cnt = queue.pop(0)
            if curr == n**2:
                return cnt
            visited.add(curr)
            for i in range(1,7):
                if curr + i > n**2:
                    continue
                next_pos = curr + i if array[curr+i] == -1 else array[curr+i]
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos,cnt+1))
        return -1
                
        