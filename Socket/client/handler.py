
def handler(sock):
    print("[+] Handler started")
    while True:
        user_input=sock.recieve_data()
        print("[+] User input is: ", user_input)
        if user_input=="exit":
            print("[+] Exiting handler")
            break