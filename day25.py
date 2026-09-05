def validate_magic_bytes(file_path):
    # Dictionary of allowed magic bytes for valid image types
    ALLOWED_SIGNATURES = {
        "PNG": b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A",
        "JPEG": b"\xFF\xD8\xFF"
    }
    try:
        with open(file_path, "rb") as f:
            file_header = f.read(8)
            for file_type, signature in ALLOWED_SIGNATURES.items():
                if file_header.startswith(signature):
                    print(f"[+] VALIDATION PASSED: File matches {file_type} magic bytes.")
                    return True
        print("[-] SECURITY EXCEPTION: Invalid file signature. Possible malicious upload.")
        return False
    except FileNotFoundError:
        print(f"[!] Error: File not found {file_path}")

if __name__ == "__main__":
    # Testing with a dummy file path (you can create a test file to verify)
    validate_magic_bytes("test_upload.jpg")