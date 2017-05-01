class Node:
    def __init__(self, data_in):
        self.data = data_in
        self.next = None
        self.prev = None


class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tmp = self.head
        self.num_nodes = 0

    def insert(self, data_in):
        new_node = Node(data_in)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.tmp = self.head

        elif data_in < self.head.data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        elif data_in > self.tail.data:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        else:
            if data_in > self.tmp.data:
                while (data_in > self.tmp.data) and (self.tmp is not self.tail):
                    self.tmp = self.tmp.next

                new_node.next = self.tmp
                self.tmp.prev.next = new_node
                new_node.prev = self.tmp.prev
                self.tmp.prev = new_node
            else:
                while (data_in < self.tmp.data) and (self.tmp is not self.head):
                    self.tmp = self.tmp.prev

                new_node.next = self.tmp.next
                new_node.prev = self.tmp
                self.tmp.next.prev = new_node
                self.tmp.next = new_node

        self.num_nodes += 1

    def delete(self, target):
        if self.head is None:
            raise ValueError("List is Empty.")
        else:
            if target > self.tmp.data:
                while self.tmp.data != target and (self.tmp is not self.tail):
                    self.tmp = self.tmp.next

                if self.tmp.data == target:
                    self.tmp.prev.next = self.tmp.next
                    self.tmp.next.prev = self.tmp.prev
                    tmp = self.tmp
                    del tmp
                else:
                    raise ReferenceError("Value " + str(target) + " is not in List.")

    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=' ')
            tmp = tmp.next
        print()

l = Linked_list()
l.insert(5)
l.insert(7)
l.insert(3)
l.insert(9)
l.insert(4)
l.print_list()
l.delete(4)
l.insert(8)
l.print_list()
