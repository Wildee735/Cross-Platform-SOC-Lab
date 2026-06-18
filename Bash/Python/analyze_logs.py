from collections import Counter

with open("failed_logins.txt", "r") as f:
    lines = f.readlines()

ips = []

for line in lines:
    words = line.split()

    for word in words:
        if "." in word:
            ips.append(word)

counter = Counter(ips)

print("=== Suspicious IPs ===")

for ip, count in counter.items():
    if count >= 3:
        print(f"{ip} -> {count} failed attempts")
