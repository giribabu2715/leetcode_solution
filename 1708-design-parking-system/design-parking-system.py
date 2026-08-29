class ParkingSystem:

    def __init__(self, big, medium, small):
        self.parking = [big, medium, small]

    def addCar(self, carType):
        index = carType - 1

        if self.parking[index] > 0:
            self.parking[index] -= 1
            return True

        return False