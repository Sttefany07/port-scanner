import socket

def scan_ports(ip):
    print(f"Escaneando puertos en {ip}...")
    for port in range(1, 1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Puerto {port} está abierto.")
        sock.close()

scan_ports('192.168.1.1')
