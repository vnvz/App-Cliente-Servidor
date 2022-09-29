import socket, threading

HEADER = 64 #Constante para número de bytes por mensagem
FORMAT = 'utf-8' #Constante para decodificar mensagens
DISCONNECT_MESSAGE = '!disconnect' #Constante para desconectar o cliente

print("## SETUP DO SERVIDOR ##")
ip = input("INSIRA UM ENDEREÇO DE IP OU 'localhost'\n")
port = 80
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET define IPV4 e SOCK_STREAM define o protocolo como TCP
server.bind((ip, port))
print ("-------------------------")

def receivedCheckSum(receivedMsg, packets, checkSum):
    # Divisao em pacotes
    c1 = receivedMsg[0:packets]
    c2 = receivedMsg[packets:2 * packets]
    c3 = receivedMsg[2 * packets:3 * packets]
    c4 = receivedMsg[3 * packets:4 * packets]

    # Calcula a soma dos pacotes recebidos, incluindo o checkSum para conferir posteriormente o resultado
    somaRecebida = bin(int(c1, 2) + int(c2, 2) + int(c3, 2) + int(c4, 2) + int(checkSum))[2:]

    # Calculo do overflow
    if len(somaRecebida) > packets:
        x = len(somaRecebida) - packets
        somaRecebida = bin(int(somaRecebida[0:x], 2) + int(somaRecebida[x:], 2))[2:]

    # Calculo do complemento da soma
    somaRecebida = ''
    for i in somaRecebida:
        if i == '1':
            somaRecebida += '0'
        else:
            somaRecebida += '1'
    return somaRecebida


def detectaErroCheckSum(somaRecebida, checkSum):
    somaFinal = bin(int(checkSum, 2) + int(somaRecebida, 2))[2:]

    compara = ''
    for i in somaFinal:
        if i == '1':
            compara += '0'
        else:
            compara += '1'

    if int(compara, 2) == 0:
        print("CheckSum recebido = 0\nMensagem recebida com sucesso!")
    else:
        print("CheckSum recebido != 0\nMensagem corrompida")

def handle_client(conn, addr):
    print(f"[*] NOVA CONEXÃO: {addr} conectado...")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            
            print(f"[{addr}] {msg}")
            conn.send("[*] ACK!".encode(FORMAT))
        
    conn.close()

def start():
    server.listen() #Começa a escutar por conexões
    print(f"[*] Escutando {ip}, {port}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn,addr))
        thread.start() #Inicia o handle_client em thread com conn e addr passados como parâmetros
        print(f"[*] CONEXÕES ATIVAS: {threading.activeCount() - 1}")
    
    
print("[*] Servidor Iniciando...")
start()