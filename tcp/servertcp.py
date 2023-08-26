import socket

server_ip = "127.0.0.1"
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print("Servidor TCP aguardando conexões...")
connection, client_address = server_socket.accept()

while True:
    data = connection.recv(1024)
    lista = [1, 1]
    d = data.decode()
    n = int(d)

    ultimo = 1
    penultimo = 1
    if (n == 1) or (n == 2):
        lista.append(1)
    else:
        count = 3
        while count <= n:
            termo = ultimo + penultimo
            penultimo = ultimo
            ultimo = termo
            count += 1
            lista.append(termo)

    response = ' -> '.join(map(str, lista))
    connection.sendall(response.encode())

    if not data:
        break

connection.close()
