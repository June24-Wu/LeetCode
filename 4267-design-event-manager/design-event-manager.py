class EventManager:

    def __init__(self, events: list[list[int]]):
        self.h = []
        self.m = {}
        for idx, p in events:
            heapq.heappush(self.h,(-p,idx))
            self.m[idx] = p

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.m[eventId] = newPriority
        heapq.heappush(self.h,(-newPriority,eventId))

    def pollHighest(self) -> int:
        while self.h:
            priority, eventid = heapq.heappop(self.h)
            if self.m.get(eventid,None) == - priority:
                self.m[eventid] = None
                return eventid
        return -1
        


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()