import os
import socket

host = "192.168.1.104"
port = 49190

class Client:
    def __init__(self,host,port):
        self.host = host
        self.port = port


    def connect(self):
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                s.connect((_client.host,_client.port))
                break
            except socket.error as e:
                print(f"Connection failed {str(e)}")

    def receive(self):
        while True:
            try:
                data = s.recv(1024).decode("utf-8")
                print(data)
                s.close()
                break
            except socket.error as e:
                print(f"Failed to receive {str(e)}")


_client = Client(host,port)
_client.connect()
_client.receive()
