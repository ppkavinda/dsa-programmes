class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.top is None

    def size(self):
        return self.size

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
        self.size += 1

    def pop(self):
        tmp = self.top.data
        tmp2 = self.top
        self.top = self.top.next
        del tmp2
        self.size -= 1
        return tmp

    def peek(self):
        return self.top.data

    def printS(self):
        tmp = self.top
        while tmp is not None:
            print(tmp.data, end=', ')
            tmp = tmp.next

s = Stack()
print(s.isEmpty())
s.push(1)
s.push(2)
print(s.pop())
s.printS()
