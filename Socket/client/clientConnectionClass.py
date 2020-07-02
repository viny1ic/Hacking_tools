import socket

chunk_size= 4*1024
class client_connection:
    def __init__(self):
        #create a TCP socket for server
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, server_ip, server_port):
        self.server_ip=server_ip
        self.server_port=server_port
        self.address=(self.server_ip,self.server_port)
        self.sock.connect(self.address)

    def send_data(self, user_input):
        sent=bytes(user_input, "utf-8")
        self.sock.send(sent)
    
    def recieve_data(self):
        self.recieved=self.sock.recv(chunk_size)
        self.data_decoded=self.recieved.decode("utf-8")
        return self.data_decoded