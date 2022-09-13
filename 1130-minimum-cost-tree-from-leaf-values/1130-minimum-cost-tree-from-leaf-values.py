class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """
        we need to find dp(left,right), left -> start index, right -> end index
        suppose p is the partition point for the arr 
        dp(left,right) = max(arr[left:p+1]) * max(arr[p+1:right+1]) + dp(left,p) + dp(p+1,right)
        we need to find dp(left,right) for all p in the range of (left,right)
        
        """
        dp = {}
        
        def helper(left,right):
            if left == right:
                return 0 
            if (left,right) in dp:
                return dp[(left,right)]
            if left + 1 == right:
                return arr[left] * arr[right]
            
            min_cost = float('inf')
            for p in range(left,right):
                cost = (max(arr[left:p+1]) * max(arr[p+1:right+1])) + helper(left,p) + helper(p+1,right)
                min_cost = min(min_cost,cost)
            
            dp[(left,right)] = min_cost
            return min_cost
        
        
        return helper(0,len(arr)-1)