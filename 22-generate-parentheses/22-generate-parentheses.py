class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        
        def backtracking(left,right,path):
            if left == 0 and right == 0:
                res.append("".join(path[:]))
            if left < 0 or right < 0 :return
            if left > right:return
            
            path.append("(")
            backtracking(left-1,right,path)
            path.pop()
            
            path.append(")")
            backtracking(left,right-1,path)
            path.pop()
        backtracking(n,n,[])
        return res
                
        