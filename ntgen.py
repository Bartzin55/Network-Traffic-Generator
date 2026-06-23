import argparse # All interface with user.
import sys # for sys.exit - Closes program
import functions # auxiliar functions
import time # for time.sleep - apply intervals between data packet transfer
import socket # all network logic
import os # for os.urandom - generate random data

parser = argparse.ArgumentParser(
    description="A Python CLI tool for generating data traffic on a network.\n\n COMMAND | DESCRIPTION | Data type and restrictions | Default",
    formatter_class=argparse.RawDescriptionHelpFormatter
)

# Destination: The user can provide a IPv4, IPv6 or a dns name.
parser.add_argument(
    'destination',
    type=str,
    help="Destination IP address or hostname or DNS name | string | No default"
)

# port: layer 4 port, if the user set to 0, the program logic its configrued to scan all ports. Only for UDP
parser.add_argument(
    '-p',
    type=functions.validate_port, 
    default=0,
    help="Destination layer 4 port | integer >= 0 and <= 65535 | Default = 0 (All ports)",
    metavar="<PORT NUMBER>"
)

# protocol: UDP or TCP protocol
parser.add_argument(
    '-t',
    type=str.lower,
    default='u',
    help="Layer 4 protocol | t/T/TCP or u/U/UDP | Default: u",
    choices=['u', 'udp', 't', 'tcp'],
    metavar="<PROTOCOL>"
)

# count: number of packets sent by the script
parser.add_argument(
    '-c',
    type=functions.validate_count, 
    default=float('inf'),
    help="Total number of packages to be sent | integer >= 0 | Default = 0 (until manually interrupted)",
    metavar="<COUNT>"
)

# interval: time interval in seconds between each packet
parser.add_argument(
    '-i',
    type=functions.validate_interval, 
    default=1,
    help="Interval in seconds between each packet | float >= 0 | Default = 1",
    metavar="<INTERVAL>"
)

# Size: packet size in bits
parser.add_argument(
    '-s',
    type=functions.validate_size, 
    default=1450,
    help="Packet size in bytes | integer >= 1, <= 65535 | Default = 1450",
    metavar="<SIZE>"
)

# if the user don't pass any argument, go to help message
if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

args = parser.parse_args()

# Applies the mandatory condition of the "-p" argument if the "-t" argument is TCP.
if args.t in ['t', 'tcp'] and args.p == 0:
    parser.error("The -p(layer 4 port) is required in a TCP transmission.")

try:
    socket_type = socket.SOCK_STREAM if args.t in ['t', 'tcp'] else socket.SOCK_DGRAM # Defines the correct protocol on the socket, according to the user's choice.
    infos = socket.getaddrinfo(args.destination, args.p, type=socket_type) 
    family, socket_type, protocol, dns_name, ip_port_destination = infos[0]
    resolved_ip = ip_port_destination[0]
    data_packet = os.urandom(args.s) # generates a data packet of the size defined by the user.
    i = 1

    match args.t: 
        case 't' | 'tcp': # if protocol == TCP
           # if family == socket.AF_INET:
            target_addr = ip_port_destination
           # else:
            #target_addr = (resolved_ip, args.p, 0, 0) #if IP is v6
            
            while args.c > 0: # iterates until the number of packets defined by the user reaches 0.
                sock = socket.socket(family, socket_type, protocol)
                sock.settimeout(3)
                sock.connect(target_addr) # handshake
                sock.sendall(data_packet) # send packet
                sock.close() # close connection
                print(f"Sent {i} {args.s}-byte data packets over TCP protocol to destination: {resolved_ip}:{args.p:05d}") # print for user
                time.sleep(args.i) # interval defined by user
                i = i+1
                args.c = args.c-1

        case 'u' | 'udp':
            sock = socket.socket(family, socket_type, protocol)
            if args.p == 0: # port scan
                args.p = 1
                while args.c > 0: # iterates until the number of packets defined by the user reaches 0.
                    if family == socket.AF_INET:
                        target_addr = (resolved_ip, args.p) # if IP is v4
                    else:
                        target_addr = (resolved_ip, args.p, 0, 0) # if IP is v6
                    
                    sock.sendto(data_packet, target_addr)
                    print(f"Sent {i} {args.s}-byte data packets over UDP protocol to destination: {resolved_ip}:{args.p:05d}") # print for user
                    
                    time.sleep(args.i) # interval defined by user
                    i = i+1
                    args.p = args.p+1
                    if args.p == 65536:
                        args.p = 1
                    args.c = args.c-1
            
            else: # user defined a specific port
                if family == socket.AF_INET:
                    target_addr = (resolved_ip, args.p) # if IP is v6
                else:
                    target_addr = (resolved_ip, args.p, 0, 0) # if IP is v6

                while args.c > 0: # iterates until the number of packets defined by the user reaches 0.
                    sock.sendto(data_packet, target_addr)
                    print(f"Sent {i} {args.s}-byte data packets over UDP protocol to destination: {resolved_ip}:{args.p:05d}") # print for user

                    time.sleep(args.i) # interval defined by user
                    i = i+1
                    args.c = args.c-1

        case _: pass

except KeyboardInterrupt:
    print("Data transfer stopped by user.")

except socket.gaierror as e:
    print(f"DNS Error: failure to resolve destination.\nException: {e}")

except (ConnectionRefusedError, BrokenPipeError, ConnectionResetError, socket.timeout) as e:
    print(f"Connection error: Network Failure.\nException: {e}.")

except Exception as e:
    print(f"Unknown error.\nException: {e}.")


