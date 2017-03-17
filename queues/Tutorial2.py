# import queue

# q = queue.Queue()
# q.enqueue("John")
# q.enqueue("Kate")
# q.enqueue("Shankar")
# q.printQ()
# q.dequeue()
# q.printQ()
# q.enqueue("Zara")
# q.printQ()
# q.enqueue("Jack")
# q.printQ()
# q.dequeue()
# q.printQ()
# q.dequeue()
# q.printQ()


class Node:
    def __init__(self, value):
        self.element = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail = node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            self.tail = None
        else:
            return self.head.element
            self.head = self.node.next
        self.length -= 1

    def isEmpty(self):
        return self.length == 0

    def printq(self):
        while self.head.next:
            print(self.head.element)

q = Queue()
q.enqueue(1)
q.enqueue(5)
q.enqueue(6)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# q.printq()