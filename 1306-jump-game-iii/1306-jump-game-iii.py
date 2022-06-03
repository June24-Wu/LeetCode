class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = [(start,arr[start])] # index : jumpVal
        # visited = [False for _ in range(len(arr))]
        # visited[start] = True
        while queue:
            index , jump = queue.pop()
            if index - jump >= 0 and arr[index - jump] != None:
                if arr[index-jump] == 0:
                    return True
                queue.append((index-jump,arr[index-jump]))
                arr[index - jump] = None
            if index + jump < len(arr) and arr[index + jump] != None:
                if arr[index+jump] == 0:
                    return True
                queue.append((index+jump,arr[index+jump]))
                arr[index + jump] = None
        return False
        