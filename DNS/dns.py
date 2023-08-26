class SimpleDNS:
    def __init__(self):
        self.services = {}

    def register_service(self, service_name, ip, port):
        self.services[service_name] = (ip, port)

    def resolve_service(self, service_name):
        return self.services.get(service_name, "Not Found")

dns_server = SimpleDNS()
dns_server.register_service("www.sitemassatcp.com", "127.0.0.1", 12345)
dns_server.register_service("www.sitemassaudp.com", "127.0.0.1", 54321)

# Cliente solicitando um serviço
requested_service = input()
service_address = dns_server.resolve_service(requested_service)
print("Endereço do serviço:", service_address)
