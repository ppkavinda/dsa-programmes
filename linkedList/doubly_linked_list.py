# double linked list implementation


# class node
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# class doubly linked list
class Doubly_Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.prob = self.head

    def insert(self, data_in):
        new_node = Node(data_in)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.prob = self.head

        elif data_in < self.head.data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        elif data_in > self.tail.data:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        else:
            tmp = self.head
            while tmp is not self.tail and tmp.data < data_in:
                tmp = tmp.next

            new_node.next = tmp.next
            tmp.next.prev = new_node
            tmp.next = new_node
            new_node.prev = tmp

    def remove(self, data):
        if self.head is None:
            return False
        elif data < self.prob.data:
            while self.prob is not None and self.prob.data != data:
                self.prob = self.prob.prev

        elif data > self.prob.data:
            while self.prob is not None and self.prob.data != data:
                self.prob = self.prob.next

        self.prob.prev = self.prob.next
        self.prob.next = self.prob.prev

        # print("Prem:", self.prob.data)

    def printL(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
        # print("P:", self.prob.data)


l = Doubly_Linked_list()
l.insert(9)
l.insert(5)
l.insert(2)
l.insert(3)
l.printL()
print("----")


