Failed Login Analyzer

A beginner-friendly Python cybersecurity project that analyzes authentication logs and identifies potentially suspicious failed-login activity.

Project Objective

The purpose of this project is to practice basic SOC analyst skills using Python.

The program:

- Reads authentication logs
- Detects failed login events
- Extracts source IP addresses
- Counts failed login attempts
- Applies a detection threshold
- Generates security alerts
- Creates a CSV investigation report

Technologies

- Python 3
- File handling
- CSV processing
- Collections / Counter
- Basic log analysis

Detection Logic

The current detection rule is:

> 5 or more failed login attempts from the same IP address are flagged as potentially suspicious.

This threshold is used for demonstration purposes and does not by itself confirm malicious activity.

Example Output

```text
=== SOC Authentication Analysis ===

IP Address: 192.168.1.10
Failed attempts: 5
Status: SUSPICIOUS
ALERT: Possible brute-force activity detected!

IP Address: 192.168.1.20
Failed attempts: 1
Status: NORMAL

Report saved as results.csv
```

Investigation Report

The analyzer generates a `results.csv` file containing:

| IP Address | Failed Attempts | Status |
|---|---:|---|
| 192.168.1.10 | 5 | SUSPICIOUS |
| 192.168.1.20 | 1 | NORMAL |

This provides a structured record of the detection results for further analysis.

SOC Investigation Concept

Repeated authentication failures can be an indicator of brute-force activity.

However, an alert does not automatically confirm that an attack occurred. A SOC analyst should investigate additional evidence such as:

- Source IP reputation
- Target accounts
- Authentication timestamps
- Successful logins after failures
- Geographic/network context
- Other security events

MITRE ATT&CK

Potentially related technique:

T1110 — Brute Force

The project is designed for educational purposes and uses synthetic log data.

What I Learned

Through this project I practiced:

- Python file handling
- Parsing authentication logs
- Extracting security indicators
- Counting failed login attempts
- Creating detection rules
- Generating SOC-style alerts
- Creating CSV investigation reports
- Thinking about alerts as indicators requiring investigation

Disclaimer

This project uses synthetic log data and is intended for educational and defensive cybersecurity purposes.L
