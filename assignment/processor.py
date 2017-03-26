# implementing class Node
class Node:
    def __init__(self, processID, size):
        self.beginAddress = 0
        self.endAddress = self.beginAddress + size - 1
        self.processID = processID
        self.hole = True
        self.next = None
        self.size = size

    def printNode(self):
        print(self.size)


# beginning of class memory
class Memory:
    def __init__(self, freeMem):
        os = Node("Operating System", 400)
        self.head.hole = False
        self.head = os

        freeSpace = Node("Free Space", freeMem+1)
        freeSpace.hole = True
        os.next = freeSpace

    def checkPExists(self, ps):
        current = self.head
        while current.next is not None:
            if current.processID == ps:
                return True
            current = current.next
        return False

    def allocate(self, pID, size):
        if self.checkPExists(pID):
            print("The process: '", pID, "' is already running.")
        else:
            current = self.head
            while current.next is not None:
                if current.hole is True:
                    freeSpace = (current.endAddress + 1) - current.beginAddress
                    if freeSpace >= size:
                        newPs = Node(pID, size)
                        newPs.beginAddress = current.beginAddress
                        newPs.endAddress = newPs.beginAddress + size - 1
                        newPs.hole = False
                        current.beginAddress = newPs.endAddress + 1
                        break

                current = current.next

    def terminate(self):
        pass

    def snapshot(self):
        pass

m = Memory(2560)
m.snapshot()
