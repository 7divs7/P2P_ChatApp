import socket

host = input("Enter host: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, 8886))

name = input("Your name: ")
print("\n---------------BLEH-------BLEH-------BLEH--------------\n")

while True:
    g=input(name+": ")
    msg=name+": "+g
    client.send(bytes(msg,"utf-8"))
    if(g=="end chat"):
        break

    from_server = b''
    data = client.recv(4096)
    if not data: break
    from_server = data
    print (from_server.decode("utf-8"))
       
client.close()
print("\nSERVER DISCONNECTED")