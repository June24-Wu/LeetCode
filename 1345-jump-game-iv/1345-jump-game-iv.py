class Solution:
    def minJumps(self, arr: List[int]) -> int:
        table = {}
        for index , num in enumerate(arr):
            if num not in table:
                table[num] = []
            table[num].append(index)
        # arrLen = len(arr)
        # top = [(0,arr[0])] ; down = [(arrLen -1,arr[-1])]  # index , val
        # arr[0] = None ; arr[-1] = None;cnt = 0
        # while top:
        #     print(top,down)
        #     if len(top) > len(down):
        #         top , down = down , top
        #     length = len(top)
        #     for _ in range(length):
        #         index , val = top.pop(0)
        #         if (index,val) in down:
        #             return cnt
        #         left = index - 1 ; right = index + 1
        #         if left >= 0 and arr[left] != None:
        #             top.append((left,arr[left]))
        #             arr[left] = None
        #         if right < len(arr) and arr[right] != None:
        #             top.append((right,arr[right]))
        #             arr[right] = None
        #         while table[val]:
        #             subIndex = table[val].pop()
        #             if subIndex == index:
        #                 continue
        #             if arr[subIndex] != None:
        #                 top.append((subIndex,val))
        #     cnt += 1
        # return -1
        queue = [(0,arr[0])]
        arr[0] = None ; cnt = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                index , val = queue.pop(0)
                if index == len(arr) - 1:
                    return cnt
                # if val == None:
                #     continue
                left = index - 1 ; right = index + 1
                if left >= 0 and arr[left] != None:
                    queue.append((left,arr[left]))
                    arr[left] = None
                if right < len(arr) and arr[right] != None:
                    queue.append((right,arr[right]))
                    arr[right] = None
                while table[val]:
                    subIndex = table[val].pop()
                    if subIndex == index:
                        continue
                    if arr[subIndex] != None:
                        queue.append((subIndex,val))
            cnt += 1
        return - 1
            
                
        