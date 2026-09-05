def analyze_dockerfile(path):
    print(f"[*] Parsing Container Directives: {path}\n")
    has_explicit_user = False
    
    try:
        with open(path, 'r') as file:
            for idx, line in enumerate(file, 1):
                cleaned = line.strip().upper()
                
                # Check for explicit USER directive
                if cleaned.startswith("USER"):
                    has_explicit_user = True
                    
                # Check for unpinned latest tag
                if cleaned.startswith("FROM") and ":LATEST" in cleaned:
                    print(f"[RISK DETECTED] Line {idx}: Root baseline uses unpinned 'latest' tag.")
                    
                # Check for exposed SSH port 22
                if "EXPOSE 22" in cleaned:
                    print(f"[CRITICAL PROHIBITED] Line {idx}: Core networking exposes SSH protocol channel (Port 22)[cite: 2].")
            
            # Check if non-compliant root execution risk is present
            if not has_explicit_user:
                print("[RISK DETECTED] Non-compliant posture: Explicit USER instructions are absent (Implicit Root execution risk)[cite: 2].")
                
    except Exception as e:
        print(f"[!] Error reading file: {e}")

if __name__ == "__main__":
    analyze_dockerfile("Dockerfile")