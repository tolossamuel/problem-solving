class UndergroundSystem(object):

    def __init__(self):
        self.checkin = defaultdict(list)
      
        self.average = defaultdict(list)


    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.checkin[id] = [stationName,t]
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.average[(self.checkin[id][0],stationName)].append((t- self.checkin[id][1]))
    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        averageTime = self.average[(startStation, endStation)]
        # print(averageTime)
        averageTime =float(sum(averageTime))/float(len(averageTime) )
        return averageTime


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)