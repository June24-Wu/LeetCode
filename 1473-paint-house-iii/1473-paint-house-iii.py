class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        ans = float("inf")
        
        @cache
        def dfs(index,numOfGroup,preColor):
            if index == len(houses):
                if numOfGroup == target:
                    return 0
                return float("inf")
            curr_color = houses[index]
            if curr_color != 0:
                if curr_color != preColor:
                    numOfGroup += 1
                return dfs(index + 1,numOfGroup,curr_color)
            else:
                total_cost = float("inf")
                for curr_color in range(1,n + 1):
                    if curr_color != preColor: 
                        total_cost = min(total_cost,cost[index][curr_color - 1] + dfs(index + 1,numOfGroup + 1,curr_color))
                    else:
                        total_cost = min(total_cost,cost[index][curr_color - 1] + dfs(index + 1,numOfGroup,curr_color))
                return total_cost
        
        ans = dfs(0,0,float("inf"))
        return ans if ans != float("inf") else -1
                
        
        
        # Backtracking TLE
#         groupcnt = 1 ; total_cost = 0 ; ans = float("inf")
#         def backtracking(index):
#             nonlocal groupcnt ; nonlocal total_cost ; nonlocal ans
#             if index == len(houses):
#                 # print(houses,total_cost,groupcnt)
#                 if groupcnt == target:
#                     ans = min(ans,total_cost)
#                 return
#             if houses[index] != 0:
#                 val = 1 if index > 0 and houses[index] != houses[index - 1] else 0
#                 groupcnt += val
#                 backtracking(index + 1)
#                 groupcnt -= val
#             else:
#                 for color in range(1,n+1):
#                     houses[index] = color
#                     total_cost += cost[index][color-1]
#                     val = 1 if index > 0 and houses[index] != houses[index - 1] else 0
#                     groupcnt += val
#                     backtracking(index + 1)
#                     total_cost -= cost[index][color-1]
#                     houses[index] = 0
#                     groupcnt -= val
            
#             return
#         backtracking(0)
#         return -1 if ans == float("inf") else ans
            
        