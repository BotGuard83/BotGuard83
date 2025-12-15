# ip_validator.py
# Purpose: Validate IPv4 addresses
# Category: Input & Validation

ip = input("Enter an IPv4 address: ")

parts = ip.split(".")

if len(parts) != 4:
    print("Invalid IP address")
else:
    valid = True
    for part in parts:
        if not part.isdigit():
            valid = False
        else:
            number = int(part)
            if number < 0 or number > 255:
                valid = False

    if valid:
        print("Valid IPv4 address")
    else:
        print("Invalid IPv4 address")
