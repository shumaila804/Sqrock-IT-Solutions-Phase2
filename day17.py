import socket

def scan_local_ports(host, ports):
    print(f"[*] Initiating Socket Sweep on: {host}")
    for port in ports:
        # Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        
        # Connect to the target host and port
        state = sock.connect_ex((host, port))
        
        if state == 0:
            print(f"[!] OPEN SERVICE DETECTED: Port {port}")
        else:
            print(f"[-] Closed/Filtered: Port {port}")
            
        sock.close()

# Executing socket sweep against common development and container ports
if __name__ == "__main__":
    scan_local_ports("127.0.0.1", [22, 80, 443, 5432, 8080])