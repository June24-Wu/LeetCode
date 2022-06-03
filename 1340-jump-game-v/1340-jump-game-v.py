class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        
        
        
        visited = {}
        def dfs(index):
            if index in visited:
                return visited[index]
            res = 1
            for i in range(1,d + 1):
                right = index + i
                if right < len(arr) and arr[index] > arr[right]:
                    res = max(res,1+dfs(right))
                else:
                    break
            for i in range(1,d + 1):
                left = index - i
                if left >=0 and arr[index] > arr[left]:
                    res = max(res,1+dfs(left))
                else:
                    break
            visited[index] = res
            return res
        result = 0
        for i in range(len(arr)):
            result = max(result,dfs(i))
        return result
                    
        