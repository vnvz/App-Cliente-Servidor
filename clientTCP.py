import socket

target_port = 80
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET define IPV4 e SOCK_STREAM define o protocolo como TCP

print("Olá, bem-vindo ao serviço de teste de mensagens.")
print("Essa aplicação realiza conexões com um servidor ou localhost.")
print ("-------------------------")

target_host = input("Insira 'localhost' ou um ip de sua escolha para conectar-se:\n")
client.connect((target_host, target_port))#Conecta no endereço de escolha do usuário e na porta 80, definidas previamente

print("Conexão ao", target_host, "bem sucedida!")
msg = input("Escreva sua mensagem a ser enviada:\n")
client.send(str.encode(msg))

resp = client.recv(4096) #Define a resposta em uma variável
print("Mensagem recebida:\n",resp.decode())
client.close()