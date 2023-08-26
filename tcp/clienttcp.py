import socket
import time


server_ip = "127.0.0.1"
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

print("Sequência de Fibonacci")
message = input("Insira a quantidade de números da Sequência de Fibonacci você deseja obter (Digite em inteiro. Ex: 1, 2, 3..): ")
start_time = time.time()
client_socket.sendall(message.encode())
received_data = client_socket.recv(1024)
end_time = time.time()

print("Sequência de Fibonacci:", received_data.decode())
print("Tempo total:", end_time - start_time, "segundos")
print("Tempo de envio:", end_time - start_time, "segundos")

client_socket.close()
