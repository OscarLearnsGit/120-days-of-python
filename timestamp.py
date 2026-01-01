from datetime import datetime

# Dictionary to count events by hour
hour_counts = {}

# Read the log file
with open('events.log', 'r') as file:
    for line in file:
        # Extract the timestamp and event type from the log line
        timestamp, event_type = line.strip().split(' - ')
        
        # Convert the timestamp to a datetime object
        event_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        
        # Extract the hour from the event time
        hour = event_time.hour
        
        # Count the events by hour
        if hour in hour_counts:
            hour_counts[hour] += 1
        else:
            hour_counts[hour] = 1 

# Print the report
print("\nTimestamp Analysis Report")
print("=" * 40)
print()

print("Events by Hour:")
print("-" * 40)

# Print each hour and its count
for hour in sorted(hour_counts.keys()):
    count = hour_counts[hour]
    
    # Flag late night activity (hours 0-5)
    if 0 <= hour <= 5:
        print(f"Hour {hour:02d}: {count} events  ⚠️ LATE NIGHT")
    else:
        print(f"Hour {hour:02d}: {count} events")

print()

# Find peak hours (max count)
max_count = max(hour_counts.values())
peak_hours = [hour for hour, count in hour_counts.items() if count == max_count]

print("Peak Activity:")
print(f"- Peak hour(s): {peak_hours} with {max_count} events each")

print()

# Count late night activity
late_night_count = sum(count for hour, count in hour_counts.items() if 0 <= hour <= 5)

print("Suspicious Activity:")
if late_night_count > 0:
    print(f"⚠️ {late_night_count} events during late night hours (00:00-05:00)")
    print("⚠️ Possible automated attack pattern")
else:
    print("✅ No late night activity detected")

print()
print(f"Total events analyzed: {sum(hour_counts.values())}")
