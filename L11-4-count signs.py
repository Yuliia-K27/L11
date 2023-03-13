import socket

# функція для підрахунку кількості слів у рядку
def count_words(message):
    words = message.split()
    return len(words)

# задаємо адресу сервера та порт
HOST = 'localhost'
PORT = 5000

# створюємо сокет і прив'язуємо його до адреси сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# запускаємо сервер та очікуємо підключення клієнта
server_socket.listen()
print(f'Server is running on {HOST}:{PORT}')

while True:
    # очікуємо з'єднання з клієнтом
    client_socket, client_address = server_socket.accept()
    print(f'Client {client_address} connected.')

    # відправляємо вітання клієнту
    welcome_message = 'Welcome to the word counter server! Please enter your message:'
    client_socket.sendall(welcome_message.encode())

    # отримуємо повідомлення від клієнта та надсилаємо відповідь з кількістю слів
    while True:
        data = client_socket.recv(1024).decode().strip()
        if not data:
            break
        word_count = count_words(data)
        response_message = f'The number of words in your message is {word_count}.'
        client_socket.sendall(response_message.encode())

    # закриваємо з'єднання з клієнтом
    client_socket.close()
    print(f'Client {client_address} disconnected.')
