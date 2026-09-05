import re

# Mock access logs simulating normal traffic and SQLi attack patterns
MOCK_ACCESS_LOGS = [
    '192.168.1.45 "GET /profile?id=5 HTTP/1.1" 200',
    '10.0.4.12 "POST /auth/login?user=admin\'%20OR%20\'1\'=\'1 HTTP/1.1" 401',
    '172.16.5.9 "GET /search?q=UNION%20SELECT%20null,password%20FROM%20users-- HTTP/1.1" 500'
]

def analyze_sqli_signatures(logs):
    print("[*] Analyzing Web Interaction Logs for SQL Injection Signatures...")
    
    # Regular expression pattern to detect common SQLi meta-characters and syntax
    sqli_regex = re.compile(r"(?i)('|--|#| UNION\s+SELECT|OR\s+\d+=\d+)")
    
    for entry in logs:
        if sqli_regex.search(entry):
            # Extracting the source IP address from the log entry
            source_ip = entry.split(' ')[0]
            print(f"[CRITICAL MALICIOUS PATTERN] Source: {source_ip} -> Log: {entry}")

if __name__ == "__main__":
    analyze_sqli_signatures(MOCK_ACCESS_LOGS)