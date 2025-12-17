
"""
IP Allowlist Security Automation Script

This script automates the process of maintaining an IP allowlist by removing
unauthorized IP addresses listed in a separate removal file.

Use case:
SOC / Blue Team automation to enforce access control and reduce manual errors.
"""

# File paths
ALLOW_LIST_PATH = "data/allow_list.txt"
REMOVE_LIST_PATH = "data/remove_list.txt"


def read_file(file_path):
    """
    Reads a file and returns a list of stripped lines.
    """
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def write_file(file_path, data):
    """
    Writes a list of strings to a file, one per line.
    """
    with open(file_path, "w") as file:
        for item in data:
            file.write(item + "\n")


def update_allowlist():
    """
    Removes unauthorized IP addresses from the allowlist.
    """
    # Read current allowlist and removal list
    allow_list = read_file(ALLOW_LIST_PATH)
    remove_list = read_file(REMOVE_LIST_PATH)

    # Track removed IPs for logging
    removed_ips = []

    # Remove unauthorized IPs safely
    for ip in remove_list:
        if ip in allow_list:
            allow_list.remove(ip)
            removed_ips.append(ip)

    # Write updated allowlist back to file
    write_file(ALLOW_LIST_PATH, allow_list)

    # Output results
    print("IP Allowlist Update Complete")
    print("----------------------------")

    if removed_ips:
        print("Removed IP addresses:")
        for ip in removed_ips:
            print(f"- {ip}")
    else:
        print("No IP addresses were removed.")

    print("\nCurrent Allowlist:")
    for ip in allow_list:
        print(f"- {ip}")


if __name__ == "__main__":
    update_allowlist()

