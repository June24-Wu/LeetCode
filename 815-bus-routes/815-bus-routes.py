class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:return 0
        routeBus = {}# routes : bus
        visited = [False for i in range(len(routes))]
        for i in range(len(routes)):
            for j in routes[i]:
                if j not in routeBus:
                    routeBus[j] = []
                routeBus[j].append(i)
        # print(routeBus)
        
        queue = routeBus[source]
        length = len(queue)
        cnt = 1
        while queue != []:
            for i in queue:
                if target in routes[i]:
                    return cnt
            for i in range(length):
                bus = queue.pop(0)
                visited[bus] = True
                buses = []
                for i in routes[bus]:
                    buses.extend(routeBus[i])
                buses = list(set(buses))
                for i in buses:
                    if visited[i] == False:
                        queue.append(i)
            length = len(queue)
            cnt += 1
        return -1
        