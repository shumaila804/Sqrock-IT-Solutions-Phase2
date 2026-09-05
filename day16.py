import requests

def verify_headers(url):
    print(f"[*] Auditing Target Headers: {url}")
    try:
        res = requests.get(url, timeout=5)
        target_headers = ["Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options"]
        
        for header in target_headers:
            if header in res.headers:
                print(f"[+] CONFIGURED: {header} > {res.headers[header][:40]}...")
            else:
                print(f"[-] VULNERABLE: Missing Security Header -> {header}")
                
    except Exception as e:
        print(f"[!] Target Unreachable: {e}")

verify_headers("http://localhost:8000")