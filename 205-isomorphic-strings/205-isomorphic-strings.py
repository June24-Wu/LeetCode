class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        left, right = [[] for _ in range(len(s))] , [[] for _ in range(len(t))]
        table1 , table2 = {} , {}
        index = 0
        for i in range(len(s)):
            ch = s[i]
            if ch not in table1.keys():
                table1[ch] = index
                left[index].append(i)
                index += 1
            else:
                left[table1[ch]].append(i)
        index = 0
        for i in range(len(t)):
            ch = t[i]
            if ch not in table2.keys():
                table2[ch] = index
                right[index].append(i)
                index += 1
            else:
                right[table2[ch]].append(i)
        return left == right
            
        