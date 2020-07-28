import socket
import threading

HEADER = 64 #first message's length
PORT = 5050
#SERVER = ""  #the ip address of the device
SERVER = socket.gethostbyname(socket.gethostname()) #Determins the ip address
ADDR = (SERVER , PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT" #client disconnected

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM) #Creating new soket
server.bind(ADDR)

def handle_client(conn , addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if mg_length:
		msg_length = int(msg_length)
		msg = conn.recv(msg_length).decode(FORMAT)
		if msg == DISCONNECT_MESSAGE:
		    connected = False

        print(f"[{addr}] {msg}")
        conn.send("MESSAGE RECIVED".encode(FORMAT)) #server sending response to client

    conn.close


def start():
    server.listen()
    print(f"[LISTINING] server is listining on {SERVER}")
    while True:
        conn , addr = server.accept()
        thread = threading.Thread(target=handle_client , args=(conn , addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[Starting] server is started")
 
