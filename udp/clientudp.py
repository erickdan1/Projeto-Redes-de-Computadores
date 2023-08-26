import socket
import time

server_ip = "127.0.0.1"
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Escolha: Pedra, Papel ou Tesoura. Escreva em minúsculo e sem espaços:")
start_time = time.time()
client_socket.sendto(message.encode(), (server_ip, server_port))
received_data, server_address = client_socket.recvfrom(1024)
end_time = time.time()

print("Mensagem recebida:", received_data.decode())
print("Tempo total:", end_time - start_time, "segundos")
print("Tempo de envio:", end_time - start_time, "segundos")

client_socket.close()
