import socket


class SimpleDNS:
    def __init__(self):
        self.services = {}

    def register_service(self, service_name, ip, port):
        self.services[service_name] = ip, port

    def resolve_service(self, service_name):
        return self.services.get(service_name, "Not Found")

    def remove_service(self, service_name):
        del self.services[service_name]


dns_server = SimpleDNS()

server_ip = "127.0.0.5"
server_port = 53

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

print(f"Servidor DNS ouvindo requisições em {server_ip}:{server_port}")

while True:
    query, client_address = server_socket.recvfrom(1024)
    q = eval(query)
    if q[0] == 'check-in':
        if dns_server.resolve_service(q[1]) == 'Not Found':
            dns_server.register_service(q[1], q[2], q[3])
            response = '200'
        else:
            response = '0'
    elif q[0] == 'check-out':
        if dns_server.resolve_service(q[1]) != 'Not Found':
            dns_server.remove_service(q[1])
            response = '200'
        else:
            response = '0'
    else:
        response = str(dns_server.resolve_service(q[0]))

    server_socket.sendto(response.encode(), client_address)

