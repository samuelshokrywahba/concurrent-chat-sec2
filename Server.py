from socket import *
from _thread import *
import threading

def recieved_thread(c):
    while True:
        x = c.recv(500)
        print("client: ", x.decode("utf=8"))

def client_thread(session):
    #recieve = threading.Thread(target=recieved_thread, arg = (session, ))
    start_new_thread(recieved_thread, (session,))
    #recieve.start()
    while True:
        session.send(input("server: ").encode("utf=8"))
################################################
socket_file_discriptor = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 7000
socket_file_discriptor.bind((host, port))
socket_file_discriptor.listen(5)

#################################################
while True:
    session, client_info = socket_file_discriptor.accept()
    print("connedcted device ip: " + client_info[0])
    #بتقوم ثيد وتحمل فوقها كود أو فانكشن
    #the function we'll make will make two threads, send and recieve
    start_new_thread(client_thread, (session, )) #to handel client
session.close()