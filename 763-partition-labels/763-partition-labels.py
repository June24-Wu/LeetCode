class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        table = {}
        for i in range(len(s)):
                table[s[i]] = i
        li = [0 for _ in range(len(s))]
        
        for i in range(len(s)):
            li[i] = table[s[i]]
        print(li)
        
        return_li = []
        
        left = 0
        right = 0
        for i in range(len(li)):
            right = max(right,li[i])
            if right == i:
                return_li.append(right - left + 1)
                left = i + 1
        return return_li
        
        