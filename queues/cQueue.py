# implementing Class circular Queue
# This is Complete


class cQueue:
    # circular queue, create circular queue by passing the maxSize
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.count = 0
        self.front = 0
        self.back = maxSize - 1
        self.items = [None for _ in range(0, maxSize)]
        # print(self.items)

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.maxSize

    def size(self):
        print(self.front, self.back, self.count)
        return self.count

    def enqueue(self, item):
        assert not self.isFull(), "Error: Cannot enqueue. Queue is Full."
        self.back = (self.back + 1) % self.maxSize
        self.count += 1
        self.items[self.back] = item


    def dequeue(self):
        assert not self.isEmpty(), "Error: Cannot dequeue from Empty Queue."
        item = self.items[self.front]
        self.front = (self.front + 1) % self.maxSize
        self.count -= 1
        return item


    def printCQ(self):
        print(self.items)
        # print(self.front, self.back, self.count, self.maxSize)

#
# c = cQueue(5)
# c.printCQ()
# c.enqueue(1)
# c.printCQ()
# c.enqueue(2)
# c.printCQ()
# c.enqueue(3)
# c.printCQ()
# c.enqueue(4)
# c.printCQ()
# c.enqueue(5)
# c.printCQ()
# # c.enqueue(10)
# c.printCQ()
# c.dequeue()
# c.printCQ()
# c.enqueue(6)
# c.printCQ()
# c.dequeue()
# c.printCQ()
# c.enqueue(7)
# c.printCQ()
# c.dequeue()
# c.printCQ()
# c.dequeue()
# c.printCQ()
# c.enqueue(8)
# c.printCQ()
# c.enqueue(9)
# c.printCQ()
# c.printCQ()
