class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [[] for i in range(n+1)]
        outdegree = [[] for i in range(n+1)]
        for i in trust:
            indegree[i[1]].append(i[0])
            outdegree[i[0]].append(i[1])
        # print(indegree)
        # print(outdegree)
        for i in range(1,len(indegree)):
            if len(indegree[i]) == n-1 and len(outdegree[i]) == 0:
                return i
        return -1
