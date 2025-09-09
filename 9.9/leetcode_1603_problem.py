class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.BigCar = big
        self.MediumCar = medium
        self.SmallCar = small
        

    def addCar(self, carType):
        if carType == 1:
            if self.BigCar > 0:
                self.BigCar -= 1
                return True
        elif carType == 2:
            if self.MediumCar > 0:
                self.MediumCar -= 1
                return True
        else:
            if self.SmallCar > 0:
                self.SmallCar -= 1
                return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)