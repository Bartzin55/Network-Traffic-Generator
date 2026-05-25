import argparse
import sys
import functions
import time
# import socket


parser = argparse.ArgumentParser(
    description="A Python CLI tool for generating data traffic on a network.\n\n COMMAND | DESCRIPTION | Data type and restrictions | Default",
    formatter_class=argparse.RawDescriptionHelpFormatter
)

parser.add_argument(
    'destination',
    type=str,
    help="Destination IP address or hostname or DNS name | string | No default"
)

parser.add_argument(
    '-p',
    type=functions.validate_port, 
    default=0,
    help="Destination layer 4 port | integer >= 0 and <= 65535 | Default = 0 (All ports)",
    metavar="<PORT NUMBER>"
)

parser.add_argument(
    '-t',
    type=str.lower,
    default='u',
    help="Layer 4 protocol | t/T/TCP or u/U/UDP | Default: u",
    choices=['u', 'udp', 't', 'tcp'],
    metavar="<PROTOCOL>"
)

parser.add_argument(
    '-c',
    type=functions.validate_count, 
    default=float('inf'),
    help="Total number of packages to be sent | integer >= 0 | Default = 0 (until manually interrupted)",
    metavar="<COUNT>"
)

parser.add_argument(
    '-i',
    type=functions.validate_interval, 
    default=1,
    help="Interval in seconds between each packet | float >= 0 | Default = 1",
    metavar="<INTERVAL>"
)

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

i = 1
try:
    match args.t:
        case 't' | 'tcp':
            if args.p == 0:
                args.p = 1
                while args.c > 0:

                    ... #TODO: socket logic for TCP data transfer

                    print(f"Sent {i} {args.s}-byte data packets over TCP protocol to destination: {args.destination}:{args.p:05d}")
                    time.sleep(args.i)
                    i = i+1
                    args.p = args.p+1
                    if args.p == 65536:
                        args.p = 1
                    args.c = args.c-1
            
            else:
                while args.c > 0:

                    ... #TODO: socket logic for TCP data transfer

                    print(f"Sent {i} {args.s}-byte data packets over TCP protocol to destination: {args.destination}:{args.p:05d}")
                    time.sleep(args.i)
                    i = i+1
                    args.c = args.c-1

        case 'u' | 'udp':
            if args.p == 0:
                args.p = 1
                while args.c > 0:

                    ... #TODO: socket logic for UDP data transfer

                    print(f"Sent {i} {args.s}-byte data packets over UDP protocol to destination: {args.destination}:{args.p:05d}")
                    time.sleep(args.i)
                    i = i+1
                    args.p = args.p+1
                    if args.p == 65536:
                        args.p = 1
                    args.c = args.c-1
            
            else:
                while args.c > 0:

                    ... #TODO: socket logic for UDP data transfer

                    print(f"Sent {i} {args.s}-byte data packets over UDP protocol to destination: {args.destination}:{args.p:05d}")
                    time.sleep(args.i)
                    i = i+1
                    args.c = args.c-1

        case _: pass

except KeyboardInterrupt:
    print("Data transfer stopped.")

#TODO: Add other socket error exceptions.