class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        
        table = collections.defaultdict(list)
        for char in logs:
            idx , status , timestamp = char.split(":")
            idx , timestamp = int(idx) , int(timestamp)
            if status == "start":
                table[idx].append(timestamp)
            else:
                start = table[idx].pop()
                diff = timestamp - start + 1
                ans[idx] += diff
                for key in table:
                    table[key] = [item + diff for item in table[key]]
        return ans
                
        