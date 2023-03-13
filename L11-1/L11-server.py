import socket

# задаємо адресу сервера та порт
HOST = 'localhost'
PORT = 5000

# створюємо сокет і прив'язуємо його до заданої адреси
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# починаємо слухати порт
server_socket.listen()

print(f'Server started on {HOST}:{PORT}')

# приймаємо з'єднання
client_socket, client_address = server_socket.accept()
print(f'Connected by {client_address}')

# надсилаємо повідомлення клієнту
client_socket.sendall(b'Hello from server')

# отримуємо повідомлення від клієнта
data = client_socket.recv(1024)
print(f'Received: {data.decode()}')

# закриваємо з'єднання
client_socket.close()
