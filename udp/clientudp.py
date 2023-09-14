import socket
import time


def query_dns(dns_ip, dns_port, domain_name):
    client_socket_dns = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket_dns.settimeout(5)  # tempo limite para a resposta

    dn = (domain_name,)
    q = str(dn)
    query = q.encode()
    client_socket_dns.sendto(query, (dns_ip, dns_port))

    try:
        response, server_address_from_dns = client_socket_dns.recvfrom(1024)
        if response:
            return response.decode()
    except socket.timeout:
        return "Timeout: O servidor não respondeu a tempo."
    finally:
        client_socket_dns.close()


busca = "www.sitemassaudp.com"

server_ip, server_port = eval(query_dns("127.0.0.5", 53, busca))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print()
print("Gerador de Senha")
print()
message = 12
message_bytes = message.to_bytes(1024, byteorder='big')
start_time = time.time()
client_socket.sendto(message_bytes, (server_ip, server_port))
received_data, server_address = client_socket.recvfrom(1024)
end_time = time.time()

print("Senha gerada:", received_data.decode())
print("Tempo total:", end_time - start_time, "segundos")
print("Tempo de envio:", end_time - start_time, "segundos")

client_socket.close()
