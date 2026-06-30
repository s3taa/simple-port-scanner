import argparse
import socket
import time
import sys
import json
import threading

## Functions ---------------------------------------------------------------------------------------------------------------------------

def check_port(port):
    s = socket.socket()
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    s.close()
    if result == 0:
        service = SERVICES.get(port, 'Unknown')
        print(f'\n{GREEN}Port {port}: OPEN ({service})')
        results.append({'port': port, 'service': service})


## Visuals ---------------------------------------------------------------------------------------------------------------------------
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

title = 'Port Scanner v1.0'
for char in title:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
print('\n')

## Scanner ---------------------------------------------------------------------------------------------------------------------------
SERVICES = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    135: 'RPC',
    139: 'NetBIOS',
    443: 'HTTPS',
    445: 'SMB',
    3306: 'MySQL',
    3389: 'RDP',
    8080: 'HTTP-Alt',
}

parser = argparse.ArgumentParser(description='A simple port scanner')
parser.add_argument('target', help='Target IP address')
parser.add_argument('--start', type=int, default=1, help='Start port')
parser.add_argument('--end', type=int, default=1000, help='End port')
parser.add_argument('--output', help='Save results to file')

args = parser.parse_args()


target = args.target
start_port = args.start
end_port = args.end
total = end_port - start_port + 1
scanned = 0
results = []
threads = []
for port in range(start_port, end_port + 1):
    t = threading.Thread(target=check_port, args=(port,))
    t.start()
    threads.append(t)
    scanned += 1
    percent = int((scanned / total) * 100)
    sys.stdout.write(f'\r{RESET}Scanning {scanned}/{total} ports... ({percent}%)')
    sys.stdout.flush()


for t in threads:
    t.join()

if args.output:
     file = open(args.output, 'w')
     json.dump(results, file)
     file.close()

if args.output:
     print(f'\n{GREEN}Scan complete, Saved {len(results)} open ports to {args.output}{RESET}')
else:
     print(f'\n{GREEN}Scan complete, Found {len(results)} open ports. {RESET}')