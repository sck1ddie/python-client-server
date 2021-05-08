#Written for python3
#Coded by ~sck1ddie`

import socket

host = str(input("Enter Local IP > "))
port = int(input("Enter Port > "))

class Server:
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def create_socket(self):
        try:
            global s
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error as e:
            print("Failed to create socket!")

    def bind_socket(self):
        try:
            s.bind((_server.host,_server.port))
            s.listen()
            print(f"Succesfully listening {_server.port}")
        except socket.error as e:
            print(f"Failed to listen port {_server.port} {str(e)}")

    def accept_socket(self):
        while True:
            try:
                conn,address = s.accept()
                conn.send(f"Welcome to the my server {address[0]} !".encode("utf-8"))
                print(f"Connection from {address[0]}")
                conn.close()
            except socket.error as e:
                print(f"Failed to accept client connection {str(e)}")


_server = Server(host,port)


_server.create_socket()
_server.bind_socket()
_server.accept_socket()
