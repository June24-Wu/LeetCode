class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        indegree = Counter()
        graph = defaultdict(list)
        
        for i in range(len(ingredients)):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])
            indegree[recipes[i]] = len(ingredients[i])
        ans = []
        while supplies:
            supply = supplies.pop(0)
            if supply in graph:
                for recipe in graph[supply]:
                    if indegree[recipe] > 0:
                        indegree[recipe] -= 1
                    if indegree[recipe] == 0:
                        ans.append(recipe)
                        supplies.append(recipe)
        return ans
                    
        