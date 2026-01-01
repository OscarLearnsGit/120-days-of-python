# Create dictonary to count IPs

ip_counts = {}

# Read and count 
with open('ssh_auth.log', 'r') as file:
    for line in file:
        if "Failed password" in line:
            # Extract IP address 
            after_from = line.split("from ")[1]
            ip = after_from.split(" port")[0]
            print(ip)
            ip_counts[ip] = ip_counts.get(ip, 0) + 1

# Print report with threat detection
print("\nSSH Brute Force Detection Report")
print("=" * 35)
print()

# Print threats (5+ attempts)
print("THREATS DETECTED")
print()

threat_count = 0
for ip, count in ip_counts.items():
    if count >= 5:
        print(f"{ip}: {count} attempts - BRUTE FORCE DETECTED")
        threat_count += 1
print()

# Print normal activity
print("Normal Activity")
for  ip, count in ip_counts.items():
    if count < 5:
        print(f"{ip}: {count} attempts(s)")

print()
print(f"Total IPs analyzed: {len(ip_counts)}")
print(f"Threats detected: {threat_count}")


