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
        self.lpNo = lpNo    # lpNo = license plate No.
        self.count = 0

# end implementing the Car


# begging of the carPrak
class carPark:
    def __init__(self, maxCars):
        self.maxCars = maxCars  # defining max size of the garage
        self.maxCars = 10
        self.carLane = Queue(maxCars)   # create carLane  q
        self.waitList = []              # create waitList (python)list
        self.printList = []

    # arrive method
    def arrive(self, lpNo):
        print("\n>>>>Arriving a car")
        if self.carLane.isFull():       # if carLane is full adding lpNo to the waiting list
            print("Car Lane is Full. Added the car 'License No: ", lpNo, "' to the waiting list.")
            self.waitList.append(lpNo)

        else:
            if len(self.waitList) is 0:     # if wait list is empty add car to car lane
                car = Car(lpNo)
                print("Car Lane is have room for ", self.maxCars - len(self.carLane.items) , "cars. Added the car 'License No: ", lpNo, "' to the Lane.")
                self.carLane.enqueue(car)
                self.printList.append(lpNo)
                # car.count += 1

            else:   # if waiting list has cars add them to the carLane
                print("Car Lane is have room for ", self.maxCars - len(self.carLane.items) , "cars. Added the car 'License No: ", lpNo, "' to the Lane from waiting list.")
                waitcar = Car(self.waitList.pop(0))
                self.carLane.enqueue(waitcar)
                waitcar.count += 1
                self.printList.append(lpNo)
                # waitcar.count += 1
        self.det()

    # departure method
    def departure(self, target):    # target = target car
        print("\n<<<<Departing  a car")
        for x in range(0, len(self.carLane.items)):
            test = self.carLane.dequeue()   # test = currently checking car
            test.count += 1
            if test.lpNo == target:             # if currently checking car is the target, skip enq process
                if x == 0:                      # if first car is the target, skip the loop and just pop first car.
                    print("Departing the car 'License No: ", test.lpNo, "'.")
                    print("The car moved '", test.count, "'times through the car lane.")
                    self.printList.pop(self.printList.index(target))
                    break
                print("Departing the car 'License No: ", test.lpNo, "'.")
                print("The car moved '", test.count, "'times through the car lane.")
                self.printList.pop(self.printList.index(target))
                continue
            else:
                self.carLane.enqueue(test)  # if not the target, enq back to the carLane

        if len(self.waitList) != 0:     # if waiting list have any cars, enq them to the carLane
            print("There is room for a car.")
            waitcar = Car(self.waitList.pop(0))
            waitcar.count += 1
            self.carLane.enqueue(waitcar)
            print("Added the car to the 'License No: ", waitcar.lpNo, "'from the waiting list.")
            self.printList.append(waitcar.lpNo)
        self.det()

    # det method for (print)details
    def det(self):
        print("Cars in wait list >>", self.waitList)
        print("Cars in carPark >>", self.printList)

    # this is the organizing function
    def execute(self):
        cmd = open("input.txt", "r")
        for line in cmd:
            aord = str.upper(line[0])
            lpNo = line[1:8]

            if aord == "A":
                if (lpNo not in self.printList) and (lpNo not in self.waitList):
                    self.arrive(lpNo)
                else:
                    print("There is a car in the car lane that has the same lpNo.")

            elif aord == "D":
                if lpNo in self.printList:
                    self.departure(lpNo)
                else:
                    print("There is no such car that has lpNo:'", lpNo, "'.")


# end of carPark

c = carPark(10)
c.execute()
