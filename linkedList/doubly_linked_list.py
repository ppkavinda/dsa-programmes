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

    # insert function WITHOUT self.prob variable
    # def insert(self, data_in):
    #     new_node = Node(data_in)
    #
    #     if self.head is None:
    #         self.head = new_node
    #         self.tail = self.head
    #         self.prob = self.head
    #
    #     elif data_in < self.head.data:
    #         new_node.next = self.head
    #         self.head.prev = new_node
    #         self.head = new_node
    #
    #     elif data_in > self.tail.data:
    #         self.tail.next = new_node
    #         new_node.prev = self.tail
    #         self.tail = new_node
    #
    #     else:
    #         tmp = self.head
    #         while tmp is not None and tmp.data < data_in:
    #             tmp = tmp.next
    #         place = tmp.prev
    #
    #         new_node.next = place.next
    #         place.next.prev = new_node
    #         new_node.prev = place
    #         place.next = new_node

# insert function with self.prob variable
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
            if data_in < self.prob.data:
                while self.prob is not self.head and data_in < self.prob.data:
                    self.prob = self.prob.prev
                    node = self.prob

                new_node.next = node.next
                node.next.prev = new_node
                node.next = new_node
                new_node.prev = node

            elif data_in > self.prob.data:
                while self.prob is not self.tail and data_in > self.prob.data:
                    self.prob = self.prob.next
                    node = self.prob.prev

                new_node.next = node.next
                node.next.prev = new_node
                node.next = new_node
                new_node.prev = node

    def remove(self, data):
        if self.head is None:
            print("Error: List is empty.")
            return False
        elif data == self.head.data:
            node = self.head
            self.head = self.head.next
            del node

        elif data == self.tail.data:
            node = self.tail
            self.tail = self.tail.prev
            del node

        elif data < self.prob.data:
            while self.prob is not None and self.prob.data != data:
                self.prob = self.prob.prev
                node = self.prob
            node.prev.next = node.next
            node.next.prev = node.prev
            del node

        elif data > self.prob.data:
            while self.prob is not None and self.prob.data != data:
                self.prob = self.prob.next
                node = self.prob

            node.prev.next = node.next
            node.next.prev = node.prev
            del node

    def printL(self):
        temp = self.head
        if temp is not None:
            while temp is not self.tail:
                print(temp.data, " ",  end='')
                temp = temp.next
            print(self.tail.data)
        else:
            print("List is Empty.")


l = Doubly_Linked_list()
l.insert(1)
l.insert(9)
l.insert(6)
l.insert(3)
l.insert(5)
l.insert(2)
l.remove(5)
l.remove(9)
l.printL()
print("----")

