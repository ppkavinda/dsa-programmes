import socket
import sys


# Create socket (allows two computer to connect)
def socket_create():
    try:
        global host
        global port
        global s
        host = socket.gethostname()
        port = int(input("port:"))
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Bind socket to port and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        socket_bind()


# Establish a connection with client (socket must be listening for them)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()


# send commands
def send_commands(conn):
    while True:
        client_response = str(conn.recv(20480), "utf-8")
        print(client_response)
        cmd = input()
        conn.send(str.encode(cmd))
        print("host:>", cmd)
        if client_response == 'exit':
            conn.close()
            s.close()
            sys.exit()
        if cmd == "exit":
            conn.close()
            s.close()
            sys.exit()


def main():
    socket_create()
    socket_bind()
    socket_accept()


main()
