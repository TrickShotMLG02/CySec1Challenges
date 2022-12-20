from binascii import hexlify, unhexlify


def bytesToMAC(mac: bytes) -> str:
    """
    Args:
        mac: Ethernet as bytes

    Returns:
        human-friendly Ethernet like 18:cf:5e:7c:54:d5
    """

    return hexlify(mac, ':').decode()


def MACToBytes(mac: str) -> bytes:
    """
    Args:
        mac: human-friendly Ethernet like 18:cf:5e:7c:54:d5
    Returns:
        byte representation of the mac
    """

    return unhexlify(mac.replace(":", ""))


def parseEthernetFrame(frame: bytes) -> tuple[str, str, int, int, bytes, int]:
    """
    Parses an Ethernet II frame
    You don't have to handle 802.1Q tags!
    Args:
        frame: ethernet frame
    Returns:
        (human-readable Dest. Ethernet, human-readable Source Ethernet src, ether_type (Type), length (of the payload in bytes), Payload, CRC32)
    """
    # TODO: Implement (look at this ↑)




    dst_mac = bytesToMAC(frame[0:6])
    src_mac = bytesToMAC(frame[6:12])
    ether_type = int.from_bytes(frame[12:14], 'big')
    length = len(frame) - 6 - 6 - 2 - 4
    payload = frame[14:-4]
    crc = int.from_bytes(frame[-4:], 'big')

    return dst_mac, src_mac, ether_type, length, payload, crc


if __name__ == "__main__":
    # bytesToMAC
    mac_bytes = b'\x18\xcf^|T\xd5'
    expected_mac = "18:cf:5e:7c:54:d5"
    result_mac = bytesToMAC(mac_bytes)
    print(
        f"bytesToMAC({mac_bytes}) = {result_mac} and should be {expected_mac}, so it {'worked!' if result_mac == expected_mac else 'did not work!'}")
    print()

    # MACToBytes
    mac = "18:cf:5e:7c:54:d5"
    expected_bytes = b'\x18\xcf^|T\xd5'
    result_bytes = MACToBytes(mac)
    print(
        f"MACToBytes({mac}) = {result_bytes} and should be {expected_bytes}, so it {'worked!' if result_bytes == expected_bytes else 'did not work!'}")
    print()

    # parseEthernetFrame
    frame = b'f> +?{r\xd2SE\xfa\x94\x08\x00E\x00\x004\x00\x01\x00\x00@\x06|\xc1\x7f\x00\x00\x01\x7f\x00\x00\x01\x005\x00\x16\x00\x00\x00\x00\x00\x00\x00\x00P\x02 \x00?\x9a\x00\x00Hello World!'
    frame = b'f> +?{r\xd2SE\xfa\x94\x08\x00E\x00\x004\x00\x01\x00\x00@\x06|\xc1\x7f\x00\x00\x01\x7f\x00\x00\x01\x005\x00\x16\x00\x00\x00\x00\x00\x00\x00\x00P\x02 \x00?\x9a\x00\x00Hello World!\x1d\x01\xd4<'
    expected_tuple = ('66:3e:20:2b:3f:7b', '72:d2:53:45:fa:94', 2048, 52,
                      b'E\x00\x004\x00\x01\x00\x00@\x06|\xc1\x7f\x00\x00\x01\x7f\x00\x00\x01\x005\x00\x16\x00\x00\x00\x00\x00\x00\x00\x00P\x02 \x00?\x9a\x00\x00Hello World!',
                      486659132)
    result_tuple = parseEthernetFrame(frame)
    print(f"Frame used:         {frame}")
    print(f"Resulting tuple:    {result_tuple}")
    print(f"Expected tuple:     {expected_tuple}")
    print(f"Worked:             {expected_tuple == result_tuple}")
