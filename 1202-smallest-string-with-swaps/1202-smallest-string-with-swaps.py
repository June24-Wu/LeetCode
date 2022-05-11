class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s = list(s)
        n = len(s)
        graph = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        for i in pairs:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        print(graph)
        group = []
        def dfs(index):
            nonlocal path
            if visited[index] == True:
                return
            visited[index] = True
            path.append(index)
            for i in graph[index]:
                dfs(i)
            return
        for i in range(len(graph)):
            if visited[i] == False:
                path = []
                dfs(i)
                group.append(path)
        for i in group:
            i.sort() # [0,3]
            char = [ord(s[j]) for j in i]
            char.sort()
            char = [chr(j) for j in char] # [b.d]

            for index,item in enumerate(i):
                s[item] = char[index]
        return "".join(s)
#         s = [ord(i) for i in s]
        
#         cnt = 0
#         flag = True
#         while flag:
#             for i in pairs:
#                 if s[i[0]] > s[i[1]]:
#                     s[i[0]] , s[i[1]] = s[i[1]] , s[i[0]]
#                 else:
#                     cnt += 1
#             if cnt == len(pairs):
#                 flag = False
#         s = [chr(i) for i in s]
#         return "".join(s)
        