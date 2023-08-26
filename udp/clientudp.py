import socket
import time

server_ip = "127.0.0.1"
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print()
print("Gerador de Senha")
print()
message = input("Digite o tamanho desejado para a senha: ")
start_time = time.time()
client_socket.sendto(message.encode(), (server_ip, server_port))
received_data, server_address = client_socket.recvfrom(1024)
end_time = time.time()

print("Senha gerada:", received_data.decode())
print("Tempo total:", end_time - start_time, "segundos")
print("Tempo de envio:", end_time - start_time, "segundos")

client_socket.close()
