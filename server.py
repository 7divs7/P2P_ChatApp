import socket

host = input("Enter host: ")
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((host, 8886))
serv.listen(5)
name = input("Your name: ")

conn, addr = serv.accept()
print("CONNECTION MADE\n\n")

print("\n---------------BLEH-------BLEH-------BLEH--------------\n")

from_client = b''
while True:
    data = conn.recv(4096)
    if not data: break
    from_client = data
    print (from_client.decode("utf-8"))
    if("end chat" in from_client.decode("utf-8")):
        break
        
    g=input(name+": ")
    msg=name+": "+g
    conn.send(bytes(msg,"utf-8"))
print ('\nCLIENT DISCONNECTED')  
conn.close()