import socket
import random
import string

server_ip = "127.0.0.1"
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print("Servidor TCP aguardando conexões...")
connection, client_address = server_socket.accept()

while True:
    data = connection.recv(1024)
    d = data.decode()
    def gerar_senha(tamanho=12):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        return senha

    tamanho_da_senha = int(d)
    senha_gerada = gerar_senha(tamanho_da_senha)

    connection.sendall(senha_gerada.encode())

    if not data:
        break

connection.close()
