class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        newBoard = []
        for i in board:
            for j in i:
                newBoard.append(str(j)) # [1,2,3,4,0,5]
        def move(board:list):
            indexOf0 = board.index("0")
            rt_li = []
            if indexOf0 % 3 == 0:
                newli = board.copy()
                newli[indexOf0] , newli[indexOf0+1] = newli[indexOf0+1] , newli[indexOf0]
                rt_li.append(newli)
                newli = board.copy()
                newli[0] , newli[3] = newli[3] , newli[0]
                rt_li.append(newli)
            elif indexOf0 % 3 == 2:
                newli = board.copy()
                newli[indexOf0] , newli[indexOf0-1] = newli[indexOf0-1] , newli[indexOf0]
                rt_li.append(newli)
                newli = board.copy()
                newli[2] , newli[5] = newli[5] , newli[2]
                rt_li.append(newli)
            else:
                newli = board.copy()
                newli[indexOf0] , newli[indexOf0-1] = newli[indexOf0-1] , newli[indexOf0]
                rt_li.append(newli)
                newli = board.copy()
                newli[indexOf0] , newli[indexOf0+1] = newli[indexOf0+1] , newli[indexOf0]
                rt_li.append(newli)
                newli = board.copy()
                newli[1] , newli[4] = newli[4] , newli[1]
                rt_li.append(newli)                
            return rt_li
        
        queue = [newBoard]
        length = len(queue)
        visited = set()
        step = 0
        while queue != []:
            if ["1","2","3","4","5","0"] in queue:
                return step
            for i in range(length):
                a = queue.pop(0)
                a = move(a)
                for i in a:
                    if "".join(i) not in visited:
                        queue.append(i)
                        visited.add("".join(i))
            length = len(queue)
            step += 1
        return -1
                
        