import socket

HEADER = 64 #Constante para número de bytes por mensagem
FORMAT = 'utf-8' #Constante para decodificar mensagens
DISCONNECT_MESSAGE = '!disconnect' #Constante para desconectar o cliente

target_port = 80
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET define IPV4 e SOCK_STREAM define o protocolo como TCP

def findCheckSum(msg, packets):
    def findCheckSum(msg, packets):
        c1 = msg[0:packets]
        c2 = msg[packets:2 * packets]
        c3 = msg[2 * packets:3 * packets]
        c4 = msg[3 * packets:4 * packets]

        # Soma todos os pacotes usando-se base 2 para obter-se o "checkSum"
        somaBinaria = bin(int(c1, 2) + int(c2, 2) + int(c3, 2) + int(c4, 2))[2:]

        # Responsavel por fazer o loop dos numeros que derem overflow checksum, caso haja
        if len(somaBinaria) > packets:
            x = len(somaBinaria) - packets
            somaBinaria = bin(int(somaBinaria[0:x], 2) + int(somaBinaria[x:], 2))[2:]
        if len(somaBinaria) < packets:
            somaBinaria = '0' * (packets - len(somaBinaria)) + somaBinaria

        checkSum = ''
        for i in somaBinaria:
            if i == '1':
                checkSum += '0'
            else:
                checkSum += '1'
        return checkSum


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT) #Envia primeiramente o tamanho da mensagem, respeitando o protocolo do servidor.
    send_length += b' ' * (HEADER - len(send_length)) #Adiciona bytes vazios para completar a mensagem, de acordo com o protocolo.
    
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT)) #Recebe o ACK e descriptografa ele.

print("Olá, bem-vindo ao serviço de teste de mensagens.")
print("Essa aplicação realiza conexões com um servidor ou localhost.")
print ("-------------------------")

target_host = input("Insira 'localhost' ou um ip de sua escolha para conectar-se:\n")
client.connect((target_host, target_port)) #Conecta no endereço de escolha do usuário e na porta 80, definidas previamente

print("Conexão ao", target_host, "bem sucedida!")

while True:
    msg = input("Escreva sua mensagem a ser enviada:\n")
    if msg == DISCONNECT_MESSAGE:
        send(DISCONNECT_MESSAGE)
        client.close()
        break
    
    send(msg)