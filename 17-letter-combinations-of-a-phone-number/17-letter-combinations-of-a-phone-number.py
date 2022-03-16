class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }
        final = []
        for i in digits:
            if final == []:
                final = table[i]
                continue
            append_li = []
            for j in final:
                for t in table[i]:
                    append_li.append(j+t)
            final = append_li
        return final
                

        