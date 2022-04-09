import socket, threading
#from funcs.py import *

print("## SETUP DO SERVIDOR ##")
ip = input(print("INSIRA UM ENDEREÇO DE IP OU 'localhost'"))
port = 80

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET define IPV4 e SOCK_STREAM define o protocolo como TCP
server.bind((ip, port))

server.listen(5) #Escuta até 5 conexões simultâneas
print("[*] Escutando", ip, port)
    
while True:
    client, addr = server.accept()
    print ("[*] Conexão aceita de:", addr[0], addr[1])
    
    data = client.recv(1024)
    if not data:
        print("[*] Fechando a conexão...")
        client.close()
        break
    
    print ("[*] Recebido:", data.decode())
    print ("-------------------------")
    
    client.send(str.encode("[*] ACK!"))
    client.send(str.encode("[*] Recebido pelo servidor!"))
    client.close()
    