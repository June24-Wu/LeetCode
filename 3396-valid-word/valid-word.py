class Solution:
    def isValid(self, word: str) -> bool:
        c = 0 ; k = 0
        if len(word) < 3:
            return False
        for i in word:
            if i in ['@', '#' , '$']:
                return False
            if i in ['a', 'e' , 'i', 'o','u',"A","E","I","O","U"]:
                c += 1
            elif i not in [str(i) for i in range(10)]:
                k += 1
        return k > 0 and c > 0

        