import socket

delimiter="<END_OF_COMMAND>"
chunk_size= 4*1024
class server_connection:
    def __init__(self):
        #create a TCP socket for server
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def create_connection(self, ip,port):
        #bind to server and listen for incoming connections
        self.server_ip=ip
        self.server_port=port
        self.address=(self.server_ip,self.server_port)
        self.sock.bind(self.address)
        self.sock.listen(10)

    def accept_connection(self):
        self.client_sock, self.client_address= self.sock.accept()
        print("[+] Connection established with client: ", self.client_address)
        return (self.client_sock, self.client_address)

    def send_data(self, user_input):
        sent=bytes(user_input, "utf-8")
        self.client_sock.send(sent)
    
    def recieve_data(self):
        self.recieved=self.client_sock.recv(chunk_size)
        self.data_decoded=self.recieved.decode("utf-8")
        return self.data_decoded

    def recieve_command(self):
        result=b''
        while True:
            chunk=self.sock.recv(chunk_size)
            if chunk.endswith(delimiter.encode()):
                chunk+=chunk[:-len(delimiter)]
                result+=chunk
                break
            result+=chunk
        print(result.decode())