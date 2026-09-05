import re

# Mock system authentication logs simulating SSH access attempts
AUTH_LOGS = [
    "Sep 05 08:12:30 server sshd[4521]: Accepted publickey for root from 192.168.1.10 port 54321 ssh2",
    "Sep 05 08:15:01 server sshd[4632]: Failed password for invalid user admin from 203.0.113.50 port 38210 ssh2",
    "Sep 05 08:15:03 server sshd[4632]: Failed password for invalid user admin from 203.0.113.50 port 38210 ssh2",
    "Sep 05 08:15:05 server sshd[4632]: Failed password for invalid user admin from 203.0.113.50 port 38210 ssh2",
    "Sep 05 08:15:07 server sshd[4632]: Failed password for invalid user admin from 203.0.113.50 port 38210 ssh2"
]

def detect_ssh_bruteforce(logs, threshold=3):
    print("[*] Analyzing System Authentication Logs for SSH Brute-Force Patterns...")
    failed_attempts = {}
    
    # Regex to extract failed login logs and source IP addresses
    fail_regex = re.compile(r"Failed password for.*from\s+([\d\.]+)")
    
    for entry in logs:
        match = fail_regex.search(entry)
        if match:
            ip = match.group(1)
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
            
    # Evaluate against the threat threshold
    for ip, count in failed_attempts.items():
        if count >= threshold:
            print(f"[CRITICAL THREAT] Potential Brute-Force Attack Detected! Source IP: {ip} -> {count} consecutive failures.")
        else:
            print(f"[-] Normal activity observed from IP: {ip} ({count} failure/s)")

if __name__ == "__main__":
    detect_ssh_bruteforce(AUTH_LOGS)