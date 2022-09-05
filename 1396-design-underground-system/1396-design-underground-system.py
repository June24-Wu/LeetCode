class UndergroundSystem:

    def __init__(self):
        self.stations_to_time = {} # (start , end) : [time1 ,time2]
        self.custmer = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.custmer[id] = [stationName,t] 

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkinStation , checkinTime  = self.custmer[id]
        if (checkinStation,stationName) not in self.stations_to_time:
            self.stations_to_time[(checkinStation,stationName)] = [0,0]
        original_time , originalcnt = self.stations_to_time[(checkinStation,stationName)]
        original_time += t - checkinTime
        self.stations_to_time[(checkinStation,stationName)] = [original_time,originalcnt+1]
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.stations_to_time[(startStation,endStation)][0] / self.stations_to_time[(startStation,endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)