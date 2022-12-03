# Name: Tim Schlachter
# Matriculation number: 7039326

from md5 import MD5


class HashLengthExtension:
    KEYLENGTH = 32
    BLOCK_SIZE = 64

    customer = None
    pizzeria = None

    def __init__(self, customer, pizzeria):
        # NO TOUCHING!!!!
        self.customer = customer
        self.pizzeria = pizzeria

    def addPadding(self, message: bytearray, length: int = 0) -> bytearray:
        '''
        Adds MD5 specific padding to bytearray with respect to the key length
        Args:
            message: message to be padded as a bytearray
            length: of some prefix (the original message + padding for example) -> 0 by default

        Returns:
            bytearray of the message + padding
        '''
        message_copy = message[:]  # copy byte_array, because else you would overwrite the original message


        messageLength = len(message_copy)
        message_copy += b'\x80'

        padLen = 512 - 64 - messageLength - 8

        for i in range(0, int(padLen/8)):
            message_copy += b'\x00'

        for i in range(0, length):
            message_copy += b'\x00'

        message_copy += int((messageLength + self.KEYLENGTH) * 8).to_bytes(8, 'little')

        return message_copy

    def attack(self):
        data_to_add = "&lat=49.259&long=7.051"

        # receive order from customer
        original_msg_b, original_hash_b = self.customer.receive() # <- NO TOUCHING!!!!
        original_msg, original_hash = original_msg_b.decode("UTF-8"), original_hash_b.decode("UTF-8")

        print("============================================")
        print("Customer:")
        print(f"Original Message:   {original_msg}")
        print(f"Original Hash:      {original_hash}")
        print("")

        # TODO: Implement hash length extension attack here (msg == request)

        # send order to pizzeria
        # send as bytes like you would do it with something like the socket lib
        self.pizzeria.send(original_msg_b, original_hash_b) # <- NO TOUCHING!!!!

        # receive answer from pizzeria
        msg, hash = self.pizzeria.receive() # <- NO TOUCHING!!!!
        print("============================================")
        print("Pizzeria:")
        print(msg.decode("UTF-8"))

if __name__ == "__main__":
    msg = "This is the best pizzeria!"
    length = 10

    hle = HashLengthExtension(None, None)
    msg_padded = hle.addPadding(bytearray(msg.encode("UTF-8")))
    expected = bytearray(
        b'This is the best pizzeria!\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd0\x01\x00\x00\x00\x00\x00\x00')

    print(f"Message:                {msg}")
    print(f"Length:                 {length}")
    print(f"Message with padding:   {msg_padded}")
    print(f"Expected:               {expected}")
    print(f"Worked:                 {msg_padded == expected}")