class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        
        colors_table = [None for _ in range(len(colors))]
        table = {}
        for idx , color in enumerate(colors):
            table[color] = idx
            dis1 = float("inf") if 1 not in table else abs(table[1] - idx)
            dis2 = float("inf") if 2 not in table else abs(table[2] - idx)
            dis3 = float("inf") if 3 not in table else abs(table[3] - idx)
            colors_table[idx] = (dis1,dis2,dis3)
        table = {}
        for idx in range(len(colors) - 1,-1,-1):
            color = colors[idx]
            table[color] = idx
            dis1 = colors_table[idx][0] if 1 not in table else min(colors_table[idx][0],abs(table[1] - idx))
            dis2 = colors_table[idx][1] if 2 not in table else min(colors_table[idx][1],abs(table[2] - idx))
            dis3 = colors_table[idx][2] if 3 not in table else min(colors_table[idx][2],abs(table[3] - idx))
            colors_table[idx] = (dis1,dis2,dis3)  
        ans = []
        for idx , color in queries:
            val = colors_table[idx][color-1] if colors_table[idx][color-1] != float("inf") else -1
            ans.append(val)
        return ans
            
            
        
        