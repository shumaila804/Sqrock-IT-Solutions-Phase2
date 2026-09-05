import re

# Mock user inputs submitted via web forms or URL parameters
USER_INPUTS = [
    "Hello, welcome to our portal!",
    "<script>alert('XSS Attack');</script>",
    "Normal search query for cybersecurity reports",
    "<img src=x onerror=alert(document.cookie)>"
]

def detect_xss_payloads(inputs):
    print("[*] Auditing User Inputs for Cross-Site Scripting (XSS) Signatures...")
    
    # Regular expression pattern to detect common script injection vectors
    xss_regex = re.compile(r"(<script.*?>.*?</script>|onerror\s*=|javascript:|<img.*?src)", re.IGNORECASE)
    
    for idx, text in enumerate(inputs, 1):
        if xss_regex.search(text):
            print(f"[MALICIOUS XSS DETECTED] Index {idx}: Payload found in input -> '{text}'")
        else:
            print(f"[SAFE INPUT] Index {idx}: Clean text -> '{text}'")

if __name__ == "__main__":
    detect_xss_payloads(USER_INPUTS)