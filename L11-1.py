import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 55000))
while True:
    sock.send(input("Message to Server: ").encode("UTF-8"))
    data = sock.recv(1024)
    print(data.decode("UTF-8"))
sock.close()