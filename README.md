# App Cliente/Servidor.

## Extras

Aplicação implementada em Python utilizando-se de sockets. Esse aplicativo é capaz de fornecer uma comunicação confiável para os dados trocados entre os sistemas finais, considerando um canal com perda de dados e erros.
**Características específicas:**
- Capaz de se conectar ao servidor através do localhost (na mesma máquina) ou via IP.
- Utiliza-se do protocolo TCP.
- Permite verificação de transporte confiável (W.I.P.)
- Falhas de integridade podem ser simuladas. (W.I.P.)
- Aceita mensagens individuais ou em grupo.

Essa aplicação foi implementada no Windows através do Subsistema Linux (WSL2).

## Como executar o programa.
Primeiramente você deve rodar o arquivo `serverTCP.py` em uma instância de terminal. Ex:
```
sudo python serverTCP.py
```
Após rodá-lo, basta apenas seguir as instruções dentro do programa.
Logo em seguida você deve rodar em outra instância do terminal o arquivo `clientTCP.py`. Ex:
```
sudo python clientTCP.py
```
Seguindo esse processo, basta seguir as instruções dentro do programa e ver ele em funcionamento. Para desconectar o cliente do servidor, apenas envie a mensagem `!disconnect`.
(placeholder para explicar processo de simulação de erros)

