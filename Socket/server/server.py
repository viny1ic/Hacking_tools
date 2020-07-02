from connectionClass import server_connection

if __name__=="__main__":
    s=server_connection()
    s.create_connection()
    conn_sock, conn_address=s.accept_connection()
    s.send_data("never gonna give you up never gonna let you down never gonna run around and desert you")
    print(s.recieve_data())
    
    
    s.sock.close()
    conn_sock.close()