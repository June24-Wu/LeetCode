class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        table = set()
        def change(s:str):
            nonlocal bank
            nonlocal table
            res = []
            s = list(s)
            for i in range(len(s)):
                originLetter = s[i]
                for j in ["A","C","G","T"]:
                    s[i] = j
                    if "".join(s) not in table and "".join(s) in bank:
                        res.append("".join(s))
                        table.add("".join(s))
                s[i] = originLetter
            return res
        
        queue = [start]
        length = len(queue)
        cnt = 0
        while queue != []:
            if end in queue:
                return cnt
            for i in range(length):
                a = queue.pop(0)
                queue.extend(change(a))
            print(queue)
            length = len(queue)
            cnt += 1
        return -1
        
            
        