standard_macs = []
clean_macs = []
lower_macs = []
char_macs = []
cisco_macs = []

# accept a list of MAC addresses as user input
print("Enter the MACs you want to convert, one per line.")
print("Type 'end' when you've entered them all:")
while True:
    mac = input()

    if mac == 'end':
        break
    else:
        standard_macs.append(mac)

# remove whitespace
for mac in standard_macs:
    clean_macs.append(mac.strip())

# convert characters to lower case
for mac in clean_macs:
    lower_macs.append(mac.lower())

# remove symbols
for mac in lower_macs:
    result = mac.replace(":", "")
    result = result.replace("-", "")
    char_macs.append(result)

# add periods
for mac in char_macs:
    result = ""
    for i in range(0, len(mac), 4):
        chunk = mac[i:i+4]
        result += chunk

        if i + 4 < len(mac):
            result += "."

    cisco_macs.append(result)

# present output
print("Standard Format: <----> Cisco Format:")
for i in range(0, len(cisco_macs)):
    print(f"{clean_macs[i]}\t{cisco_macs[i]}")
