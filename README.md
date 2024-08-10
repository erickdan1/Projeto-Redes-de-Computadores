# MultiProtocol-Password-Service

Este repositório contém uma aplicação de sockets cliente-servidor desenvolvida para oferecer um serviço de geração de senhas. A aplicação está implementada em duas versões, utilizando os protocolos UDP (User Datagram Protocol) e TCP (Transmission Control Protocol). Além disso, inclui um servidor DNS simples, responsável por registrar os domínios dos servidores e responder às requisições dos clientes. Ao término do serviço, o domínio do servidor é removido do DNS.

## Visão Geral

- **Protocolos Utilizados**: 
  - **UDP**: Protocolo de comunicação orientado para a velocidade, sem garantias de entrega de pacotes.
  - **TCP**: Protocolo de comunicação confiável, garantindo a entrega de pacotes na ordem correta.

- **Componentes**:
  - **Servidor**: Responsável por gerar e enviar senhas para os clientes.
  - **Cliente**: Envia requisições ao servidor e recebe as senhas geradas.
  - **Servidor DNS**: Registra e gerencia os domínios dos servidores, além de atender às requisições dos clientes.

## Executando a Aplicação

Para rodar a aplicação, siga a ordem correta de execução:

1. **Servidor DNS**: Inicie o servidor DNS, que será responsável por registrar os domínios dos servidores.
2. **Servidor**: Inicie o servidor com o protocolo desejado (UDP ou TCP).
3. **Cliente**: Execute o cliente com o mesmo protocolo do servidor.

**Nota**: Certifique-se de que tanto o servidor quanto o cliente estão configurados para utilizar o mesmo protocolo (ambos UDP ou ambos TCP) para garantir a compatibilidade.

## Funcionamento

Abaixo, um diagrama de fluxo ilustrando o funcionamento da aplicação:

![Diagrama de fluxo](https://github.com/erickdan1/Projeto-Redes-de-Computadores/assets/115114338/da4f41f0-8ba3-46a2-926e-6457ec77b135)

---
