# Failed IP checker

LOG_DATA = """
2024-11-04 08:23:11 - Failed login from 192.168.1.50
2024-11-04 08:24:33 - Failed login from 10.0.0.5
2024-11-04 08:25:12 - Failed login from 192.168.1.50
2024-11-04 08:27:45 - Failed login from 172.16.0.100
2024-11-04 08:28:03 - Failed login from 192.168.1.50
2024-11-04 08:30:22 - Failed login from 10.0.0.5
2024-11-04 08:31:56 - Failed login from 192.168.1.50
2024-11-04 08:33:14 - Failed login from 8.8.8.8
2024-11-04 08:35:28 - Failed login from 10.0.0.5
2024-11-04 08:37:41 - Failed login from 192.168.1.50
"""
LOG_PREFIX = "Failed login from "

def analyze_failed_logins(log_content):

    ip_counts = {}

    print("Starting analysis of hardcoded log data...")
    print("-" * 40)

    for line in log_content.splitlines():
        clean_line = line.strip() 

        if clean_line and LOG_PREFIX in clean_line:
            ip_address = clean_line.split(LOG_PREFIX)[1].strip()

            ip_counts[ip_address] = ip_counts.get(ip_address, 0) + 1

    print("Failed Login Attempts by IP Address:")
    print("-" * 35)  

    for ip, count in sorted(ip_counts.items()):
        print(f"| {ip:<15} | attempts :{count}")

    print("_" * 35)
    print(f"Total Unique Ips tracked {len(ip_counts)}")

if __name__ == "__main__":
    analyze_failed_logins(LOG_DATA)
