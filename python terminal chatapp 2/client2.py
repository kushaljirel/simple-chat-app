import socket

PORT = 5050

HEADER = 100

SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)

FORMAT = 'utf-8'

DISCONNECT_MSG = "DISCONNECTED!!"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


mess = input('Enter your message: \n')
mess2 = f"{SERVER}: {mess}"
send(mess2)    
send(DISCONNECT_MSG)


