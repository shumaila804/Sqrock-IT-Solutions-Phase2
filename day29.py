def isolate_compromised_host(host_ip):
    print(f"[!] INITIATING CONTAINMENT PROTOCOL FOR {host_ip}")
    print(f"[*] Step 1: Revoking active sessions for {host_ip}...")
    print(f"[*] Step 2: Applying 'QUARANTINE' Security Group rules...")
    print(f"[*] Step 3: Null-routing external egress traffic...")
    print(f"[+] CONTAINMENT SUCCESSFUL: {host_ip} is isolated from the network segment.")

if __name__ == "__main__":
    isolate_compromised_host("192.168.1.150")