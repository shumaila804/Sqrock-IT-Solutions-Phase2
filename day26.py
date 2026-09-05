import re

class WAFMiddleware:
    def __init__(self):
        # Ruleset targeting common web attack vectors (XSS, SQLi, Path Traversal)
        self.rules = [
            (re.compile(r"(?i)<script>"), "XSS Attempt"),
            (re.compile(r"(?i)union\s+select"), "SQLi Attempt"),
            (re.compile(r"(?i)\.\./\.\./"), "Path Traversal")
        ]
        
    def inspect_payload(self, request_data):
        for pattern, rule_name in self.rules:
            if pattern.search(request_data):
                print(f"[WAF BLOCK] Dropped request. Triggered Rule: {rule_name}")
                return False
        print("[WAF ALLOW] Payload is clean.")
        return True

if __name__ == "__main__":
    waf = WAFMiddleware()
    # Testing WAF inspection with a traversal exploit payload
    waf.inspect_payload("GET /image?file=../../etc/passwd HTTP/1.1")