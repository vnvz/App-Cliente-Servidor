import socket, threading
#from funcs.py import *

HEADER = 64 #Constante para número de bytes por mensagem
FORMAT = 'utf-8' #Constante para decodificar mensagens
DISCONNECT_MESSAGE = '!disconnect' #Constante para desconectar o cliente

print("## SETUP DO SERVIDOR ##")
ip = input("INSIRA UM ENDEREÇO DE IP OU 'localhost'\n")
port = 80
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET define IPV4 e SOCK_STREAM define o protocolo como TCP
server.bind((ip, port))

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
    server.listen(5) #Escuta até 5 conexões simultâneas
    print(f"[*] Escutando {ip}, {port}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn,addr))
        thread.start() #Inicia o handle_client em thread com conn e addr passados como parâmetros
        print(f"[*] CONEXÕES ATIVAS: {threading.activeCount() - 1}")
    
    
print("[*] Servidor Iniciando...")
start()