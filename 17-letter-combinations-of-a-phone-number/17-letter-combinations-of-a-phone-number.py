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
        
        ######## first ###################
        # final = []
        # for i in digits:
        #     if final == []:
        #         final = table[i]
        #         continue
        #     append_li = []
        #     for j in final:
        #         for t in table[i]:
        #             append_li.append(j+t)
        #     final = append_li
        # return final
        
        
        ######## second ###################
        
        return_li = []
        length = len(digits)
        if length == 0:return[]
        def backtracking(start_index,path):
            if len(path) == length:
                return_li.append("".join(path))
                return
            for item in table[digits[start_index]]:
                path.append(item)
                backtracking(start_index+1,path)
                path.pop()
        backtracking(0,[])
        return   return_li
        
            
                

        