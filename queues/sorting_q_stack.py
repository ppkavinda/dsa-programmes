# import queue
# from acdm_workspace.dsa.stacks import stack


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


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, ele):
        self.items.append(ele)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def printStack(self):
        print(self.items)


def sort():
    q = Queue()
    s = Stack()

    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(20)
    q.enqueue(60)
    q.enqueue(10)

    q.printQ()
    s.printStack()
    print("|||||||||||||||||")
    a = 1

    if s.isEmpty():
        s.push(q.dequeue())

    while not s.isEmpty():
        if q.peek() > s.peek():
            s.push(q.dequeue())
            print("2")
        else:
            q.enqueue(s.pop())
            print("3")
        s.printStack()
        q.printQ()

        print(">>", a, "<<")
        a += 1
sort()