# implementing the liner Queue class
# This is complete


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

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
        print(self.items)
# end implementing the queue


# implementing the car obj
class Car:
    def __init__(self, lpNo):
        self.lpNo = lpNo
        self.count = 0
# end implementing the Car


class carPark:
    maxCars = 10
    carLane = Queue()




carPark()
