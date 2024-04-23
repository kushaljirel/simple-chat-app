import socket
import threading

PORT = 5050

HEADER = 100

SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)

FORMAT = 'utf-8'

DISCONNECT_MSG = "DISCONNECT!!"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

# msg = 

def handle_clinet(conn, addr):
    print(f'[NEW CONNECTIONS] {addr} connected.')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            print(f'[{addr}]: {msg}')
            mess = input('Enter your message: \n')
            mess2 = f"[SERVER]: {mess}".encode(FORMAT)
            conn.send(mess2)

    conn.close()


def start():
    server.listen()
    print(f"[SERVER] is listening at {SERVER}.")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clinet, args=(conn, addr))
        thread.start() 
        print(f"[ACTIVE CONNECTION] = {threading.activeCount() - 1}")


print("***SERVER IS STARTING....****\n")
start()
