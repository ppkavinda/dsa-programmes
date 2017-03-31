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
        self.printList = []
        self.lpNo = 0

    def arrive(self, lpNo):
        print(">>>>Arriving a car")
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

    # departure method
    def departure(self, target):    # target = target car
        if target in self.printList:
            print("<<<<Departing  a car")
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
        else:
            print("There is no such car that has lpNo:'", target, "'.")

    # det method for (print)details
    def det(self):
        print("------------------")
        print("wtlist", self.waitList)
        print(self.printList)
        print("\n----------------")


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
cp.arrive("E10")
# cp.arrive(11)
# cp.arrive(12)
# cp.departure(5)
# cp.departure(9)
# cp.arrive(12)
# cp.arrive(13)
# cp.arrive(14)
# cp.departure(1)
# cp.departure(8)
cp.departure("E0")
cp.departure(2)

cp.det()