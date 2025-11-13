
import socket, os, sys

packetcount = 1 # only for counting the number of packages sent / somente para fazer a contagem de pacotes enviados
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Lines for formatting the program in the terminal / linhas para formatação do programa no terminal
def hashtag_line():
    print("###########################################################################")

def line():
    print("--------------------------------------------------")

#presentation / apresentacao
hashtag_line()
print()
print("                        Network Traffic Generator")
print("Repositório GitHub: https://github.com/Bartzin55/Network-Traffic-Generator")
print()
hashtag_line()

#ip/hostname reequest / solicitação do ip/hostname
ip_or_hostname = input("Digite o IP (Ipv4 apenas)/Hostname de destino: ")

#port request / solicitação da porta
strport = input("Digite a porta: ")

#user input validation / validação da entrada do usuário
try:
    port = int(strport)
except (ValueError):
    print("Valor inválido.")
    sys.exit()

#destination in a tuple (ip, port) / destino em uma tupla (ip, porta)
destination = (ip_or_hostname,port)

#random data generation / geração de dados aleatórios
packet = os.urandom(1472)

#sending packets / enviando pacotes
while True:
    sock.sendto(packet,destination)
    print(f"Enviando {packetcount} pacotes de dado de 1472 bytes para {ip_or_hostname}:{port}")
    packetcount += 1
