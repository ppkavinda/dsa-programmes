import socket

s = socket.socket()
host = socket.gethostname()
port = int(input("port:"))
s.connect((host, port))

while True:
    cmd = input()
    if len(str.encode(cmd)) > 0:
        s.send(str.encode(cmd))
        print("host:>", cmd)
        client_response = str(s.recv(20480), "utf-8")
        print(client_response)
        if client_response == 'exit':
            s.close()
    if cmd == "exit":
        s.close()
