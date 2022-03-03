class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table1 , table2 = {} , {}
        for i in s:
            table1[i] = table1[i] +1 if i in table1.keys() else 1
        for i in t:
            table2[i] = table2[i] +1 if i in table2.keys() else 1
        return table1 == table2
            
        