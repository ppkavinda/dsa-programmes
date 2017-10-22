import socket
import threading


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        if self.threadID == 1:
            rev()
        else:
            snd()
        print("Exiting " + self.name)


s = socket.socket()
host = socket.gethostname()
port = int(input("port:"))
s.connect((host, port))


def rev():
    while True:
        client_response = str(s.recv(20480), "utf-8")
        if len(client_response) > 0:
            print(client_response)
            if client_response == 'exit':
                s.close()


def snd():
    while True:
        cmd = input()
        if len(str.encode(cmd)) > 0:
            s.send(str.encode(cmd))
            print("host:>", cmd)

        if cmd == "exit":
            s.close()


thread1 = myThread(1, "rev", 1)
thread2 = myThread(2, "snd", 2)

thread1.start()
thread2.start()
