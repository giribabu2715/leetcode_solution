class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.trips = {}

    def checkIn(self, id, stationName, t):
        self.check_in[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        startStation, startTime = self.check_in[id]

        travelTime = t - startTime

        key = (startStation, stationName)

        if key not in self.trips:
            self.trips[key] = [0, 0]

        self.trips[key][0] += travelTime
        self.trips[key][1] += 1

        del self.check_in[id]

    def getAverageTime(self, startStation, endStation):
        key = (startStation, endStation)

        totalTime = self.trips[key][0]
        totalTrips = self.trips[key][1]

        return totalTime / totalTrips