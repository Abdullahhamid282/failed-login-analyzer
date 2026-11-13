from collections import Counter

log_file = "sample_logs.txt"

failed_ips = []

with open(log_file, "r") as file:
    for line in file:
        if "FAILED_LOGIN" in line:
            parts = line.split("ip=")
            ip = parts[1].strip()
            failed_ips.append(ip)

ip_counts = Counter(failed_ips)

print("=== SOC Authentication Analysis ===")

for ip, count in ip_counts.items():

    if count >= 5:
        status = "SUSPICIOUS"
    else:
        status = "NORMAL"

    print(f"\nIP Address: {ip}")
    print(f"Failed attempts: {count}")
    print(f"Status: {status}")
