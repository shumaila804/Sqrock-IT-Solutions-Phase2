import json

def aggregate_reports(json_files):
    unified_findings = []
    print("[*] Aggregating Vulnerability Scans from multiple sources...")
    
    # Mocking reading from multiple tool outputs (e.g., Bandit, Trivy)
    mock_data = [
        {"tool": "Bandit", "vuln": "Hardcoded Password", "severity": "HIGH"},
        {"tool": "Trivy", "vuln": "Outdated Base Image Package", "severity": "MEDIUM"}
    ]
    
    for issue in mock_data:
        if issue['severity'] == "HIGH":
            unified_findings.append(issue)
            print(f"[+] Aggregated HIGH-RISK: {issue['vuln']} (Source: {issue['tool']})")
        else:
            print(f"[-] Filtered out lower severity: {issue['vuln']} (Source: {issue['tool']})")
            
    return unified_findings

if __name__ == "__main__":
    aggregate_reports(["bandit_out.json", "trivy_out.json"])