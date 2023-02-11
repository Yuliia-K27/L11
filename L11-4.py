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
    s = data.decode("UTF-8")
    n = len(s.split())
    conn.send(bytes("Кількість слів у введеній фразі: " + str(n), encoding = "UTF-8"))
conn.close
