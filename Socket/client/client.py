from clientConnectionClass import client_connection

if __name__=="__main__":
    s=client_connection()
    s.connect("192.168.2.7", 7777)
    ans=s.recieve_data()
    print(ans)
    s.send_data("you rickrolled me")
    s.sock.close()