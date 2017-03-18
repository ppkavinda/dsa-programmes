# import queue
# from acdm_workspace.dsa.stacks import stack


class Queue:
    def __init__(self):
        self.qitems = []

    def isEmpty(self):
        return len(self.qitems) == 0

    def enqueue(self, item):
        self.qitems.append(item)

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        return self.qitems.pop(0)

    def size(self):
        return len(self.qitems)

    def peek(self):
        return self.qitems[len(self.qitems) - 1]

    def printQ(self):
        print(self.qitems)


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
    q.enqueue(80)
    q.enqueue(70)

    q.printQ()
    s.printStack()
    print("|||||||||||||||||")
    a = 1

    while not q.isEmpty():
        if s.isEmpty() or (s.peek() < q.peek()):
            s.push(q.dequeue())
        else:
            q.enqueue(s.pop())

        q.printQ()
        s.printStack()
        print("---------")
sort()
