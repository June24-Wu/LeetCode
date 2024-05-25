class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_m = collections.defaultdict(int)
        balls = {}
        color_set = set() ; ans = []
        for ball , color in queries:
            if ball in balls:
                original_color = balls[ball]
                color_m[original_color] -= 1
                if color_m[original_color] == 0:
                    color_set.remove(original_color)
            balls[ball] = color
            color_set.add(color)
            color_m[color] += 1
            ans.append(len(color_set))
        return ans


                
        