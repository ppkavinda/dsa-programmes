# implementing class Node
class Node:
    def __init__(self, processID, size):
        self.beginAddress = None
        self.endAddress = None
        self.processID = processID
        self.size = size
        self.hole = True
        self.next = None

    def printNode(self):
        print(self.data)


# beginning of class memory
class Memory:
    def __init__(self, freeMem):
        self.beginAddress = 0
        self.endAddress = 2560
        self.pID = None
        self.freeMem = freeMem
        self.head = None

        os = Node("Operating System", 400)
        self.head = os
        os.next = None

    def checkPExists(self, ps):
        current = self.head
        while current.next is not None:
            if current.processID == ps:
                return True
            else:
                return False
            current = current.next

    def allocate(self, pID, size):
        if self.checkPExists(pID):
            print("The process: '", pID, "' is already running.")
        else:
            ps = Node(pID, size)

        pass

    def terminate(self):
        pass

    def snapshot(self):
        pass

m = Memory(2560)
m.snapshot()
