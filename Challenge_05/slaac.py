def convert(mac: str, prefix: str) -> str:
    """
    Args:
        mac: You know this one
        prefix: network prefix (64 bit) with ":" at the end
    Returns:
        IPv6 address
    """
    # TODO: Implement
    pass


if __name__ == "__main__":
    mac = "00:0c:f1:8e:c1:d8"
    prefix = "fe80:0000:0000:0000:"

    expected_address = "fe80:0000:0000:0000:020c:f1ff:fe8e:c1d8"
    result_address = convert(mac, prefix)
    print(
        f"convert({mac, prefix}) = {result_address} and should be {expected_address}, so it {'worked!' if result_address == expected_address else 'did not work!'}")
