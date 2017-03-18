# code from labSheet 3, /// complete and working


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def strnode(self):
        print(self.data)
# ///////////////////////////////////////////////
# implementing linked list //code from labSheet 3


class LinkedList:
    def __init__(self):
        self.numnodes = 0  # The number of the nodes in linked list
        self.head = None  # reference to the first node

    # create and insert a new node to the front of the linkedList
    def insertFirst(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.numnodes += 1

    # create and insert a new node to the back of the linkedList
    def insertLast(self, data):
        newNode = Node(data)
        newNode.next = None  # because newNode is the last node
        if self.head is None:  # checking weather the list is empty
            self.head = newNode  # if empty, newNode is the head
            return

        lnode = self.head  # lnode is a tmp reference to get to the last node
        while lnode.next is not None:  # getting last node
            lnode = lnode.next
        lnode.next = newNode  # new node is now the last node
        self.numnodes += 1

    # remove node from the front of the linkedList
    def remFirst(self):
        cnode = self.head  # cnode >> current node
        self.head = cnode.next  # new head is the second node
        cnode.next = None  # breaking the connection of first node with second node
        del cnode
        self.numnodes -= 1

    # remove node from the back of the linkedList
    def remLast(self):
        lnode = self.head
        while lnode.next is not None:
            pnode = lnode
            lnode = lnode.next
        pnode.next = None
        del lnode
        self.numnodes -= 1

    # get the value of the first node
    def getFirst(self):
        lnode = self.head
        return lnode.data

    # get the value of the last node
    def getLast(self):
        lnode = self.head
        while lnode.next is not None:
            lnode = lnode.next
        return lnode.data

    # printing the linkedList
    def print_list(self):
        lnode = self.head
        while lnode:
            lnode.strnode()  # print the node
            lnode = lnode.next

    def getSize(self):
        return self.numnodes

print("New linked list")
listObj2017 = LinkedList()
listObj2017.insertFirst("Wickramasinghe")
listObj2017.insertFirst(99)
listObj2017.insertFirst(45)
listObj2017.print_list()
# listObj2017.insertLast(78)
# listObj2017.insertLast(88)
# listObj2017.insertLast("Sirisena")
print("Remove first node")
listObj2017.remFirst()
print("remove last node")
listObj2017.remLast()
listObj2017.print_list()
