import struct


def parseIPv4Header(header: bytes) -> tuple[list[int, int, int, int, int, int, int, int, int, int, int, int, int, bytes], bytes]:
    """
    Parses an IPv4 header.
    Args:
        header: IPv4 header
    Returns:
        ([version, header_length, type_of_service, total_length, identification, flag_mf, flag_df, fragment_offset,
            ttl, proto, checksum, source_addr, dest_addr, options_and_padding], payload)
    """
    # TODO: Implement
    pass


def reassembleFragments(fragments: list[bytes]) -> bytes:
    """
    Reassembles IPv4 payload from fragments.
    Args:
        fragments: list of fragments
    Returns:
        assembled payload
    """
    # TODO: Implement
    pass


if __name__ == "__main__":
    # Test parseIPv4Header
    header = b'F\x00\x00 \x00* \x00\x80\x11\x08\x9e\x7f\x00\x00\x01\x01\x01\x01\x01\x03\x03\x10\x00~\xe0\x00P\x00(\n\x05'

    expected_tuple = (
        [4, 6, 0, 32, 42, 1, 0, 0, 128, 17, 2206, 2130706433, 16843009, b'\x03\x03\x10\x00'], b'~\xe0\x00P\x00(\n\x05')
    result_tuple = parseIPv4Header(header)

    print(f"Header:             {header}")
    print(f"Resulting tuple:    {result_tuple}")
    print(f"Expected tuple:     {expected_tuple}")
    print(f"Worked:             {expected_tuple == result_tuple}")
    print()

    # Test reassembleFragments
    fragments = [
        b'F\x00\x00 \x00* \x00\x80\x11\x08\x9e\x7f\x00\x00\x01\x7f\x00\x00\x01\x03\x03\x10\x00~\xe0\x00P\x00(\n\x05',
        b'F\x00\x00 \x00* \x02\x80\x11\x08\x9c\x7f\x00\x00\x01\x7f\x00\x00\x01\x03\x03\x10\x00cheap. S',
        b'F\x00\x00 \x00* \x01\x80\x11\x08\x9d\x7f\x00\x00\x01\x7f\x00\x00\x01\x03\x03\x10\x00Talk is ',
        b'F\x00\x00 \x00* \x03\x80\x11\x08\x9b\x7f\x00\x00\x01\x7f\x00\x00\x01\x03\x03\x10\x00how me t',
        b'F\x00\x00 \x00*\x00\x04\x80\x11(\x9a\x7f\x00\x00\x01\x7f\x00\x00\x01\x03\x03\x10\x00he code.'
    ]

    expected_payload = b'~\xe0\x00P\x00(\n\x05Talk is cheap. Show me the code.'
    result_payload = reassembleFragments(fragments)

    print(f"Fragments:          {fragments}")
    print(f"Resulting payload : {result_payload}")
    print(f"Expected payload:   {expected_payload}")
    print(f"Worked:             {expected_payload == result_payload}")
