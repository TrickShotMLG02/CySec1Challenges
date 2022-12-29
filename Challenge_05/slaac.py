# Name: Tim Schlachter
# Matriculation number: 7039326

def convert(mac: str, prefix: str) -> str:
    """
    Args:
        mac: You know this one
        prefix: network prefix (64 bit) with ":" at the end
    Returns:
        IPv6 address
    """

    # Flipping 7th bit of first byte
    binaryFlipped = bin(int(mac[0:2], 16) ^ 2)
    hexFlipped = hex(int(binaryFlipped, 2))
    resultingMac = str(hexFlipped)[2:].zfill(2) + mac[2:]

    # Inserting FF:FE in middle of string
    MacLength = len(resultingMac)
    resultingMac = resultingMac[0:int(MacLength/2+1)] + "ff:fe" + resultingMac[int(MacLength/2):]

    # Removing every second : (beginning with the first one)

    resultingMac = resultingMac[0:2] + resultingMac[3:6] + resultingMac[6:8] + resultingMac[9:12] + resultingMac[12:14] + resultingMac[15:18] + resultingMac[18:20] + resultingMac[21:25]

    lladdr = prefix + resultingMac

    return lladdr


if __name__ == "__main__":
    mac = "00:0c:f1:8e:c1:d8"
    prefix = "fe80:0000:0000:0000:"

    expected_address = "fe80:0000:0000:0000:020c:f1ff:fe8e:c1d8"
    result_address = convert(mac, prefix)
    print(
        f"convert({mac, prefix}) = {result_address} and should be {expected_address}, so it {'worked!' if result_address == expected_address else 'did not work!'}")
