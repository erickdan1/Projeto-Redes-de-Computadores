import socket
import random
import string


url_domain = "www.sitemassatcp.com"

server_ip = "127.0.0.3"
server_port = 12345

dns_ip = "127.0.0.5"
dns_port = 53

# Registrar domínio no servidor DNS
def registrar_dns(url, s_ip, s_port):
    global dns_ip, dns_port

    client_socket_dns = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket_dns.settimeout(5)  # tempo limite para a resposta

    d = 'check-in', url, s_ip, s_port
    q = str(d)
    query = q.encode()
    client_socket_dns.sendto(query, (dns_ip, dns_port))

    try:
        response, server_address_from_dns = client_socket_dns.recvfrom(1024)
        if response.decode() == '200':
            print('O domínio foi registrado com sucesso.')
        else:
            print('Não foi possível registrar o domínio.')

    except socket.timeout:
        return "Timeout: O servidor não respondeu a tempo."
    finally:
        client_socket_dns.close()


def remove_dns(url):
    global dns_ip, dns_port

    client_socket_dns = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket_dns.settimeout(5)  # tempo limite para a resposta

    d = 'check-out', url
    q = str(d)
    query = q.encode()
    client_socket_dns.sendto(query, (dns_ip, dns_port))

    try:
        response, server_address_from_dns = client_socket_dns.recvfrom(1024)
        if response.decode() == '200':
            print('O domínio foi removido com sucesso.')
        else:
            print('Não foi possível remover o domínio.')

    except socket.timeout:
        return "Timeout: O servidor não respondeu a tempo."
    finally:
        client_socket_dns.close()


registrar_dns(url_domain, server_ip, server_port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print("Servidor TCP aguardando conexões...")
connection, client_address = server_socket.accept()

while True:
    data = connection.recv(1024)

    def gerar_senha(tamanho=12):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        return senha

    tamanho_da_senha = int.from_bytes(data, byteorder='big')
    senha_gerada = gerar_senha(tamanho_da_senha)

    connection.sendall(senha_gerada.encode())

    if not data:
        break

remove_dns(url_domain)

connection.close()
print('Conexão TCP encerrada')