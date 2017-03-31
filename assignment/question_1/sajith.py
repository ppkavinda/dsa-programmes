#please do not copy this entire code, go through it get and understanding and try to do it yourself


#the partition class, similar to Node class in linked list
class Partition:
    def __init__(self,p_id,data):
        self.startLoc = 0
        self.endLoc = self.startLoc+data-1
        self.processID = p_id
        self.isHole = True
        self.next = None


class memManage:
    def __init__(self,memSize):
        #memSize is the RAM size, here it is 2560k
        #head will be the O/S part of the memory, which is initialized at the start (0 to 399k, including 0)
        self.head = Partition("Operating System",400)
        self.head.isHole=False #since used by O/S isHole status becomes false
        #temp would be the initial stage (memory from 400k to 2560k)
        temp = Partition(-1,memSize+1)
        temp.startLoc=self.head.endLoc+1
        self.head.next=temp
        
    #function to see if process exists
    def pExists(self,p_id):
        part = self.head
        while(part != None):
            if(part.processID == p_id):
                return True
            part = part.next
        return False
            
    def allocate(self,p_id,data):  
        curr_p = self.head
        if(self.pExists(p_id)== False):#checking if partition with processID p_id exists
            while(curr_p):#loops till all partitions end
                if(curr_p.isHole == True):#checking if the partition is a free space
                    #finding if there is space to put process
                    space = (curr_p.endLoc+1)-curr_p.startLoc
                    if(data<space):
                        new_p = Partition(-1,data)          #create empty partition
                        new_p.next = curr_p.next            #point new_p next to previous partition next
                        curr_p.next = new_p                 #point previous partion next to new_p
                        new_p.endLoc=curr_p.endLoc  
                        curr_p.endLoc = curr_p.startLoc+data-1
                        curr_p.isHole = False
                        curr_p.processID = p_id
                        new_p.startLoc = curr_p.endLoc+1
                        break
                else:
                    curr_p = curr_p.next
        else:#if partition with processID p_id exists below statement will be printed
            print("Process P"+str(p_id)+" already exists!")

    def terminate(self,p_id):
        part = self.head
        found = False #found becomes true if the processID with p_id exists (we can terminate a process only if it exists)
        while(part.next != None):
            if(part.processID == p_id):#if process id exists
                part.isHole = True #isHole becomes true
                part.processID = -1 #and process id becomes -1
                found = True
            part = part.next
        if(found == False):
            print("Process "+str(p_id)+" does not exist.")
        #combining all free spaces
        part = self.head
        while(part.next != None):
            if(part.isHole == True and part.next.isHole == True):
                part.endLoc=part.next.endLoc
                part.next=part.next.next
                continue
            else:
                part = part.next


    def printMem(self):
        c_p = self.head #c_p :- current partition
        while(c_p != None):
            if(c_p.processID != -1):
                print(str(c_p.startLoc)+"k - "+str(c_p.endLoc)+"k : "+str(c_p.processID))
            else:
                print(str(c_p.startLoc)+"k - "+str(c_p.endLoc)+"k : Free Space")
            c_p = c_p.next


    
new = memManage(2560)
new.allocate("P1",600)
new.allocate("P2",1000)
new.allocate("P3",300)
new.terminate("P2")
new.allocate("P4",700)
new.terminate("P1")
new.allocate("P5",400)
new.printMem()


#test with new.terminate("P4")
#the free spaces that are near each other should then combine and become one free space

