# Name: Tim Schlachter
# Matriculation number: 7039326

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
    version = int.from_bytes(header[0:1], 'big') >> 4
    header_length = int.from_bytes(header[0:1], 'big') & 0b00001111
    type_of_service = int.from_bytes(header[1:2], 'big')
    total_length = int.from_bytes(header[2:4], 'big')
    identification = int.from_bytes(header[4:6], 'big')
    flag_mf = (int.from_bytes(header[6:7], 'big') & 0b00100000) >> 5
    flag_df = (int.from_bytes(header[6:7], 'big') & 0b01000000) >> 6
    fragment_offset = (int.from_bytes(header[6:8], 'big') & 0b0001111111111111)
    ttl = int.from_bytes(header[8:9], 'big')
    proto = int.from_bytes(header[9:10], 'big')
    checksum = int.from_bytes(header[10:12], 'big')
    source_addr = int.from_bytes(header[12:16], 'big')
    dest_addr = int.from_bytes(header[16:20], 'big')
    options_and_padding = header[20:(20 + header_length * 4 - 20)]
    payload = header[(20 + header_length * 4 - 20):]

    return ([version, header_length, type_of_service, total_length, identification, flag_mf, flag_df, fragment_offset, ttl, proto, checksum, source_addr, dest_addr, options_and_padding], payload)


def reassembleFragments(fragments: list[bytes]) -> bytes:
    """
    Reassembles IPv4 payload from fragments.
    Args:
        fragments: list of fragments
    Returns:
        assembled payload
    """

    # Since the offset is stored in index 7 of the parsed header, we sort the fragments by the index 7
    sortedFragments = sorted(fragments, key=lambda x: x[7])

    # Since the payload is in the second part of the touple we extract it by
    resultingPayload = b''
    for f in list(sortedFragments):
        resultingPayload += parseIPv4Header(f)[1]

    return resultingPayload


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
