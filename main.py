def main():
    mac = input("Enter a MAC: ")
    mac = remove_whitespace(mac)
    standard_format = mac
    mac = make_lowercase(mac)
    mac = remove_colons(mac)
    mac = add_periods(mac)
    cisco_format = mac
    print("Standard MAC Format ---> Cisco MAC Format")
    print("=========================================")
    print(f"{standard_format} -----> {cisco_format}")


def remove_whitespace(mac):
    result = mac.strip()
    return result


def make_lowercase(mac):
    result = mac.lower()
    return result


def remove_colons(mac):
    result = mac.replace(":", "")
    return result


def add_periods(mac):
    result = ""

    for i in range(0, len(mac), 4):
        chunk = mac[i:i+4]
        result += chunk

        if i + 4 < len(mac):
            result += "."

    return result


main()
