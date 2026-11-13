Failed Login Analyzer

A beginner-friendly Python cybersecurity project that analyzes
authentication logs and identifies potentially suspicious
failed-login activity.

Project Objective

The purpose of this project is to practice basic SOC analyst
skills using Python.

The program:

- Reads authentication logs
- Detects failed login events
- Extracts source IP addresses
- Counts failed login attempts
- Applies a detection threshold
- Generates a security alert for potentially suspicious activity

Technologies

- Python 3
- File handling
- Collections / Counter
- Basic log analysis

Detection Logic

The current detection rule is:

> 5 or more failed login attempts from the same IP address
> are flagged as potentially suspicious.

Example Output

=== SOC Authentication Analysis ===

IP Address: 192.168.1.10
Failed attempts: 5
Status: SUSPICIOUS
ALERT: Possible brute-force activity detected!

IP Address: 192.168.1.20
Failed attempts: 1
Status: NORMAL