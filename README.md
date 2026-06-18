# Cross-Platform SOC Incident Detection & Response Lab

## Overview

This project demonstrates a Security Operations Center (SOC) workflow by collecting logs from Windows and Linux systems, detecting suspicious authentication activity, and generating incident investigation artifacts.

The project showcases practical skills in:

* Python Log Analysis
* PowerShell Automation
* Bash Scripting
* Windows Security Monitoring
* Linux Authentication Log Analysis
* Incident Response
* Threat Detection

---

## Project Architecture

```text
Windows Security Logs
        |
        v
PowerShell Script
        |
        v
CSV Export

Linux Auth Logs
        |
        v
Bash Collection Script
        |
        v
Python Analysis Engine
        |
        v
Suspicious IP Detection
```

---

## Repository Structure

```text
Cross-Platform-SOC-Lab/
│
├── Bash/
│   └── collect_logs.sh
│
├── Python/
│   └── analyze_logs.py
│
├── PowerShell/
│   └── failed_logins.ps1
│
├── logs/
│   └── failed_logins.txt
│
├── Reports/
│   └── Incident_Report.md
│
└── README.md
```

---

## Scripts

### Bash

Collect failed SSH authentication attempts from Linux logs.

```bash
./collect_logs.sh
```

### Python

Analyze failed login logs and identify suspicious IP addresses.

```bash
python analyze_logs.py
```

### PowerShell

Export Windows failed login events (Event ID 4625).

```powershell
.\failed_logins.ps1
```

---

## Sample Detection Output

```text
=== Suspicious IPs ===
192.168.1.10 -> 3 failed attempts
```

---

## Incident Response Workflow

1. Detect suspicious activity
2. Investigate source IP
3. Contain threat
4. Eradicate malicious activity
5. Recover systems
6. Document lessons learned

---

## MITRE ATT&CK Mapping

| Technique | Description                       |
| --------- | --------------------------------- |
| T1110     | Brute Force                       |
| T1078     | Valid Accounts                    |
| T1059     | Command and Scripting Interpreter |

---

## Skills Demonstrated

* SOC Operations
* Threat Hunting
* Log Analysis
* Security Monitoring
* Python Automation
* PowerShell Automation
* Bash Scripting
* Incident Response

---

## Author

Aniket Upadhyay

Aspiring SOC Analyst | Threat Hunter | Penetration Tester
