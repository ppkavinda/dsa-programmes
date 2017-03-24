# implementing the liner Queue class
# This is complete


class Queue:
    def __init__(self, maxSize):
        self.items = []
        self.maxSize = maxSize

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.maxSize

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]

    def printQ(self):
        return self.items
        print(self.items)
# end implementing the queue


# implementing the car obj
class Car:
    def __init__(self, lpNo):
        self.lpNo = lpNo
        self.count = 0

    def inf(self):  # TODO
        return self.lpNo
# end implementing the Car


# begging of the carPrak
class carPark:
    def __init__(self, maxCars):
        self.maxCars = maxCars
        self.maxCars = 10
        self.carLane = Queue(maxCars)
        self.waitList = []
        self.lpNo = 0

    def arrive(self, lpNo):
        print("Arriving a car")
        self.lpNo = lpNo
        if self.carLane.isFull():
            print("Car Lane is Full. Added the car 'License No: ", lpNo, "' the waiting list.")
            self.waitList.append(lpNo)

        else:
            if len(self.waitList) is 0:
                car = Car(self.lpNo)
                print("Car Lane is NOT Full. Added the car 'License No: ", lpNo, "' to the Lane.")
                self.carLane.enqueue(car)
                car.count += 1

            else:
                print("Car Lane is NOT Full. Added the car 'License No: ", lpNo, "' to the Lane from waiting list.")
                waitcar = Car(self.waitList.pop(0))
                self.carLane.enqueue(waitcar)
                self.count += 1

    def departure(self, cr):
        print("Departing  a car")
        for _ in range(1, 10):
            test = self.carLane.dequeue()
            if test.lpNo is cr:
                print("Departing the car 'License No: ", test.lpNo, "'.")
                print("The car moved '", test.count, "'times through the car lane.")
                continue
            else:
                self.carLane.enqueue(test)
        if len(self.waitList) is not 0:
            print("There is room for a car.")
            waitcar = Car(self.waitList.pop(0))
            self.carLane.enqueue(waitcar)
            print("Added the car to the 'License No: ", test.lpNo, "'from the waiting list.")

    def det(self):
        print ("_-_-_-_-_-_-_-_-_-")
        print ("wtlist", self.waitList)
        print ("carlist", self.carLane.items[0].lpNo, self.carLane.items[1].lpNo, self.carLane.items[2].lpNo, self.carLane.items[3].lpNo, self.carLane.items[4].lpNo, self.carLane.items[5].lpNo, self.carLane.items[6].lpNo, self.carLane.items[7].lpNo, self.carLane.items[8].lpNo,)
        print ("-_-_-_-_-_-_-_-_-_")


# end of carPark

cp = carPark(10)
cp.arrive(1)
cp.arrive(2)
cp.arrive(3)
cp.arrive(4)
cp.arrive(5)
cp.arrive(6)
cp.arrive(7)
cp.arrive(8)
cp.arrive(9)
cp.arrive(10)
# cp.arrive(11)
# cp.arrive(12)
cp.departure(1)
cp.det()
