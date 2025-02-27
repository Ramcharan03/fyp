import re

# List of vulnerability patterns
VULNERABILITIES = {
    "Reentrancy Attack": r"call.value\(",
    "Integer Overflow and Underflow": r"SafeMath|unchecked\(",
    "Unchecked External Call Return Values": r"(\.call\(|\.delegatecall\(|\.send\()",
    "Denial of Service (DoS) with Revert": r"require\(.+\)",  
    "Denial of Service (DoS) with Gas Limit": r"while\s*\(|for\s*\(",
    "Front-Running": r"block\.timestamp|now",
    "Timestamp Dependence": r"block\.timestamp|now",
    "Unprotected Self-Destruct": r"selfdestruct\(|suicide\(",
    "Delegatecall to Untrusted Contracts": r"delegatecall\(",
    "Access Control Issues": r"onlyOwner|modifier\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\(",
    "Uninitialized Storage Variables": r"storage\s+[a-zA-Z_][a-zA-Z0-9_]*;",
    "Short Address Attack": r"msg\.data\.length",
    "Floating Pragma Vulnerability": r"pragma solidity \^",
    "Tx.origin Authentication Flaw": r"tx\.origin",
    "Storage Collision in Proxy Contracts": r"assembly\s*\{",
    "Blockhash Dependence": r"block\.blockhash",
    "Poor Randomness Using on-chain Data": r"keccak256\(abi\.encodePacked\(",
    "Gas Limit Manipulation": r"gasleft\(",
    "Insufficient Signature Verification": r"ecrecover\(",
    "Improper Handling of Ether Transfers": r"payable\s*\(",
    "Unrestricted Selfdestruct Calls": r"selfdestruct\(",
    "Race Conditions in Multi-User Contracts": r"mapping\s*\(",
    "Logic Bugs in Smart Contracts": r"assert\(",
    "Approval Double-Spending Attack": r"approve\(",
    "Lack of Event Emission for Critical Actions": r"event\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\(",
}

def scan_solidity_file(file_path):
    detected_vulnerabilities = []
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line_num, line in enumerate(lines, start=1):
            for vuln_name, pattern in VULNERABILITIES.items():
                if re.search(pattern, line):
                    detected_vulnerabilities.append((line_num, vuln_name, line.strip()))

        if detected_vulnerabilities:
            print("\n🔴 Vulnerabilities Found:\n")
            for vuln in detected_vulnerabilities:
                print(f"⚠️ Line {vuln[0]}: {vuln[1]} -> {vuln[2]}")
        else:
            print("\n✅ No vulnerabilities detected!")

    except FileNotFoundError:
        print("❌ Error: Solidity file not found.")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

if __name__ == "__main__":
    solidity_file = input("Enter the Solidity file path (.sol): ")
    scan_solidity_file(solidity_file)
