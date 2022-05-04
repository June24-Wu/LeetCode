class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:return -1
        if target == "0000":return 0 
        lock = ["0000"]
        deadends = set(deadends)
        visited = set()
        

        def turning(lock_list:str):
            lock_list = list(lock_list)
            new_li = []
            for i in range(len(lock_list)):
                origin = int(lock_list[i])
                upVal = origin + 1 if origin + 1 <= 9 else 0
                lock_list[i] = str(upVal)
                new_li.append("".join(lock_list[:]))
                downVal = origin - 1 if origin - 1 >= 0 else 9
                lock_list[i] = str(downVal)
                new_li.append("".join(lock_list[:]))
                lock_list[i] = str(origin)
            return new_li

        step = 0
        length = len(lock)
        while lock != []:
            for i in range(length):
                a = lock.pop(0) 
                a = turning(a)
                for i in a:
                    if i not in deadends and i not in visited:
                        lock.append(i)
                        visited.add(i)
            length = len(lock)
            step += 1
            if target in lock: return step
        return -1