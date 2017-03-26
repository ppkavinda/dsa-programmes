# implementing class Node
class Node:
    def __init__(self, processID, size):
        self.beginAddress = 0
        self.endAddress = self.beginAddress + size - 1
        self.processID = processID
        self.hole = True
        self.next = None


# beginning of class memory
class Memory:
    def __init__(self, freeMem):
        os = Node("Operating System", 400)
        self.head = os
        freeSpace = Node("Free Space", freeMem+1)
        os.next = None
        self.head.hole = False

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
