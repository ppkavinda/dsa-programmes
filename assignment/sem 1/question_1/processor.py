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
        print(self.beginAddress, "K - ", self.endAddress, "K :", self.processID)


# beginning of class memory
class Memory:
    def __init__(self, freeMem):
        self.head = Node("Operating System", 400)
        self.head.hole = False
        freeSpace = Node("Free Space", freeMem+1)
        freeSpace.hole = True
        freeSpace.beginAddress = self.head.endAddress + 1
        self.head.next = freeSpace

    def checkPExists(self, ps):
        current = self.head
        while current is not None:
            if current.processID == ps:
                return True
            current = current.next
        return False

    def allocate(self, pID, size):
        if self.checkPExists(pID) is True:
            print("The process: '", pID, "' is already running.")

        else:
            current = self.head
            while current is not None:
                if current.hole is True:
                    freeSpace = (current.endAddress + 1) - current.beginAddress
                    if freeSpace >= size:
                        newPs = Node("Free Space", size)
                        newPs.next = current.next
                        current.next = newPs
                        newPs.endAddress = current.endAddress
                        current.endAddress = current.beginAddress + size - 1
                        current.processID = pID
                        current.hole = False
                        newPs.beginAddress = current.endAddress + 1
                        break

                current = current.next

    def terminate(self, pID):
        current = self.head
        while current is not None:
            if current.processID == pID:
                if current.next.hole is True:
                    current.endAddress = current.next.endAddress
                    current.next = current.next.next
                current.hole = True
                current.processID = "Free Space"
                return
            current = current.next
        print("Process ID '", pID, "' is not found.")

    def snapshot(self):
        current = self.head
        print("-----SNAPSHOT-----")
        while current is not None:
            current.printNode()
            current = current.next


m = Memory(2560)
m.allocate("P1", 600)
m.allocate("P2", 1000)
m.allocate("P3", 300)
m.terminate("P2")
m.allocate("P4", 700)
m.terminate("P1")
m.allocate("P5", 400)
m.snapshot()
