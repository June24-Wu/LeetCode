class Solution:
    def racecar(self, target: int) -> int:
        heap = deque()
        heap.append((0,0,1))
        # table = set()
        while heap:
            cnt , curr , speed = heap.popleft()
            # if curr in table:
            #     continue
            if curr == target:
                return cnt
            # table.add(curr)
            # if curr + speed == target:
            #     return cnt + 1
            heap.append((cnt+1,curr + speed , speed * 2))
            if (curr + speed > target and speed >0) or (curr + speed < target and speed <0):
                if speed > 0:
                    heap.append((cnt+1,curr , -1))
                else:
                    heap.append((cnt+1,curr , 1))
        return
#     def racecar(self, target: int) -> int:
#         q = deque()
#         q.append((0,1,0)) #curr pos, curr speed, number of moves
        
#         while q:
#             cp,cs,nm = q.popleft()
            
#             if cp==target:
#                 return nm
            
#             #every pos we have 2 choice
#             #A or R
            
#             #Acceleration
#             q.append((cp+cs,cs*2,nm+1))
            
#             #Reverse
#             if (cp+cs>target and cs>0) or (cp+cs<target and cs<0):
#                 if cs<0:
#                     q.append((cp,1,nm+1))
#                 else:
#                     q.append((cp,-1,nm+1))
            
            