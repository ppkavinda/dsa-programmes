import threading

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        if self.threadID == 1:
            print_time1(self.counter)
        else:
            print_time2(self.counter)
        print("Exiting " + self.name)


def print_time1(counter):
    while counter:
        t = input()
        print(t)
        counter -= 1


def print_time2(counter):
    while counter:
        for i in range(100):
            print(i)
        counter -= 1


# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread")
