import socket

# задаємо адресу сервера та порт (на який ми з'єднаємось)
HOST = 'localhost'
PORT = 5000

# створюємо сокет і з'єднуємось з сервером
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# отримуємо повідомлення від сервера
data = client_socket.recv(1024)
print(f'Received: {data.decode()}')

# надсилаємо повідомлення серверу
client_socket.sendall(b'Hello from client')

# закриваємо з'єднання
client_socket.close()
