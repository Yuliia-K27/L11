import socket

# задаємо адресу сервера та порт, на якому він буде слухати
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

# надсилаємо привітання клієнту
client_socket.sendall(b'Hello! How can I help you?')

# отримуємо повідомлення від клієнта і надсилаємо відповідь
while True:
    data = client_socket.recv(1024)
    message = data.decode().strip()

    if message.lower() == 'hi':
        client_socket.sendall(b'Hello there!')
    elif message.lower() == 'how are you?':
        client_socket.sendall(b'I am doing well, thank you.')
    elif message.lower() == 'what is your name?':
        client_socket.sendall(b'My name is Bot. How can I help you?')
    elif message.lower() == 'bye':
        client_socket.sendall(b'Goodbye!')
        break
    else:
        client_socket.sendall(b'Sorry, I did not understand that. Can you please repeat?')

# закриваємо з'єднання
client_socket.close()
