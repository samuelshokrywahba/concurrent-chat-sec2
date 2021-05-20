from socket import *
from _thread import *
import threading

socket_file_discriptor = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 7000

def recieved_thread(c):
    while True:
        x=c.recv(500)
        print(x.decode("utf=8"))
socket_file_discriptor.connect((host, port))
#recieve = threading.Thread(target=recieved_thread, arg=(socket_file_discriptor,))
#recieve.start()
start_new_thread(recieved_thread, (socket_file_discriptor,))

while True:
    socket_file_discriptor.send(input("client: ").encode("utf=8"))


