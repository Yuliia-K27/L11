import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 55000))
sock.listen(10)
print("Server is running, please, press ctrl+c to stop")
while True:
    conn, addr = sock.accept()
    print("Connected:", addr)
    data = conn.recv(1024)
    print(data.decode("UTF-8"))
    conn.send(input("Message to Client: ").encode("UTF-8"))
