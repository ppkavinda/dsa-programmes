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
        print(">>>>Arriving a car")
        if self.carLane.isFull():       # if carLane is full adding lpNo to the waiting list
            print("Car Lane is Full. Added the car 'License No: ", lpNo, "' to the waiting list.")
            self.waitList.append(lpNo)

        else:
            if len(self.waitList) is 0:     # if wait list is empty add car to car lane
                car = Car(lpNo)
                print("Car Lane is have room for ", self.maxCars - len(self.carLane.items) - 1, "cars. Added the car 'License No: ", lpNo, "' to the Lane.")
                self.carLane.enqueue(car)
                self.printList.append(lpNo)
                # car.count += 1

            else:   # if waiting list has cars add them to the carLane
                print("Car Lane is have room for ", self.maxCars - len(self.carLane.items) - 1, "cars. Added the car 'License No: ", lpNo, "' to the Lane from waiting list.")
                waitcar = Car(self.waitList.pop(0))
                self.carLane.enqueue(waitcar)
                self.printList.append(lpNo)
                # waitcar.count += 1

    # departure method
    def departure(self, target):    # target = target car
        print("<<<<Departing  a car")
        for _ in range(0, len(self.carLane.items)):
            test = self.carLane.dequeue()   # test = currently checking car
            test.count += 1
            if test.lpNo is target:             # if currently checking car is the target, skip enq process
                print("Departing the car 'License No: ", test.lpNo, "'.")
                print("The car moved '", test.count, "'times through the car lane.")
                self.printList.pop(0)
                continue
            else:
                self.carLane.enqueue(test)  # if not the target, enq back to the carLane

        if len(self.waitList) is not 0:     # if waiting list have any cars, enq them to the carLane
            print("There is room for a car.")
            waitcar = Car(self.waitList.pop(0))
            waitcar.count += 1
            self.carLane.enqueue(waitcar)
            print("Added the car to the 'License No: ", waitcar.lpNo, "'from the waiting list.")

    # det method for (print)details
    def det(self):
        print ("------------------")
        print ("wtlist", self.waitList)
        print(self.printList)

        print ("\n----------------")

    def execute(self):

        print("***Car Park Example***")
        print("*****instructions*****")
        print("Enter A, D or E")
        print("A <license number> for Arrive\nD <license number> for departure\nE for exit")
        print("(ex: A 1)")
        print("**********************\n")
        while True:

            try:
                cmd = input("A <license No> / D <license No> / E\n>")
                cmd = str.upper(cmd)
                cmdList = cmd.split(" ")

                if cmdList[0] == "A":
                    cmdList[1] = int(cmdList[1])
                    if cmdList[1] not in self.printList:
                        self.arrive(cmdList[1])
                    else:
                        print("There is a car in the car lane that has the same lpNo.")

                elif cmdList[0] == "D":
                    cmdList[1] = int(cmdList[1])
                    if cmdList[1] in self.printList:
                        self.departure(cmdList[1])
                    else:
                        print("There is no such car that has lpNo:'", cmdList[1], "'.")
                elif cmd == "E":
                    break
                else:
                    print("Invalid input.")
            except:
                print("Invalid Input. Please Enter correct format.")
            finally:
                print("-------------------------------------------\n")
                self.det()
                pass

# end of carPark

c = carPark(10)
c.execute()
