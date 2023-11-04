class UndergroundSystem:

    def __init__(self):
        self.customer = {}
        self.trip = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station, time = self.customer[id]
        if (station, stationName) in self.trip:
            self.trip[(station, stationName)][0] += (t - time)
            self.trip[(station, stationName)][1] += 1
        else:
            self.trip[(station, stationName)] = [(t - time), 1]
            
        del self.customer[id]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        averageTime = self.trip[(startStation, endStation)][0] / self.trip[(startStation, endStation)][1]
        
        
        return averageTime
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)