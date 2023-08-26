import socket
import secrets

server_ip = "127.0.0.1"
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

print("Servidor UDP aguardando mensagens...")

while True:
    data, client_address = server_socket.recvfrom(1024)
    d = data.decode()
    ppt = ['pedra', 'papel', 'tesoura']
    escolha_aleatoria = secrets.choice(ppt)
    result = ''

    if d == escolha_aleatoria:
        result = 'empatou mizeravi'
    elif d == ppt[0] and escolha_aleatoria == ppt[2]:
        result = 'tesoura! ganhasse boy, pedra ganha de tesoura'
    elif d == ppt[0] and escolha_aleatoria == ppt[1]:
        result = 'papel! hihi perdesse, papel embrulha pedra'
    elif d == ppt[1] and escolha_aleatoria == ppt[0]:
        result = 'pedra! você ganhou, papel embrulha pedra'
    elif d == ppt[1] and escolha_aleatoria == ppt[2]:
        result = 'tesoura! perdeu playba, tesoura corta papel'
    elif d == ppt[2] and escolha_aleatoria == ppt[0]:
        result = 'papel! err você ganhou, tesoura corta papel'
    elif d == ppt[2] and escolha_aleatoria == ppt[1]:
        result = 'pedra! kkkk tá sem sorte, pedra quebra tesoura'

    server_socket.sendto(result.encode(), client_address)
