# Last updated: 2/20/2026, 12:12:16 AM
1class ParkingSystem:
2
3    def __init__(self, big: int, medium: int, small: int):
4        self.parking_lot = [big, medium, small]
5
6    def addCar(self, carType: int) -> bool:
7        if self.parking_lot[carType - 1] != 0:
8            self.parking_lot[carType - 1] -= 1
9            return True
10        else:
11            return False
12
13# Your ParkingSystem object will be instantiated and called as such:
14# obj = ParkingSystem(big, medium, small)
15# param_1 = obj.addCar(carType)