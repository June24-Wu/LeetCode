class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # def isPalindrome(start_index,end_index,s):
        #     item = s[start_index:end_index]
        #     # if item == "":return False
        #     left = 0
        #     right = len(item) - 1
        #     while left < right:
        #         if item[left] == item[right]:
        #             left += 1
        #             right -= 1
        #         else:
        #             return False
        #     return True
        
        
        def isPalindrome(i: int, j: int,s):
            if i >= j:
                return True
            return isPalindrome(i + 1, j - 1,s) if s[i] == s[j] else False

        
        
        final = []
        length = len(s)
        
        def backtracking(start_index,path):
            if start_index == length:
                final.append(path[:])
                return
            for i in range(start_index,length):
                if isPalindrome(start_index,i,s):
                    path.append(s[start_index:i+1])
                    backtracking(i+1,path)
                    path.pop()
            return
        backtracking(0,[])
        return final
        
        