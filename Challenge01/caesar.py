# Name: Tim Schlachter
# Matriculation number: 7039326

def decrypt(cipher: str, shift: int) -> str:
    '''
    Args:
        cipher: ciphertext
        shift: shift used
    Returns:
        Decrypted plaintext
    '''
    possible_chars = [chr(i) for i in range(32, 127)]

    # Constants for defining the range of the allowed chars
    MIN_CHAR_ID = 32
    MAX_CHAR_ID = 127

    shiftedCipher = ""
    for c in cipher:
        if possible_chars.index(c):
            chrId = ord(c)

            while True:

                if shift > MAX_CHAR_ID - MIN_CHAR_ID:
                    shift = shift - (MAX_CHAR_ID - MIN_CHAR_ID)
                else:
                    if chrId - shift < MIN_CHAR_ID:
                        tmp = chrId - MIN_CHAR_ID
                        chrId = MAX_CHAR_ID - (shift - tmp)

                        if chrId >= MIN_CHAR_ID:
                            shiftedCipher += (chr(int(chrId)))
                            break

                    else:
                        shiftedCipher += (chr(int(chrId - shift)))
                        break

    return shiftedCipher


def getShift(cipher: str, en_dictionary: str) -> int:
    '''
    Args:
        cipher: ciphertext
    Returns:
        Shift that was used for this encryption
    '''
    possible_chars = [chr(i) for i in range(32, 127)]

    # Constants for defining the range of the allowed chars
    MIN_CHAR_ID = 32
    MAX_CHAR_ID = 127
    MAX_SHIFT = MAX_CHAR_ID - MIN_CHAR_ID


    shiftCounter = 0
    tmpPlainText = cipher

    while shiftCounter < MAX_SHIFT:
        tmpPlainText = decrypt(cipher, shiftCounter)

        #Remove all chars except letters, spaces and symbols which are usually not in a word or sentence
        alphFilter = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ %<>#@\'')
        res = ''.join(filter(alphFilter.__contains__, tmpPlainText))
        splittedPlain = res.split(" ")

        for word in splittedPlain:
            evalBool = True

            if not en_dictionary.__contains__(word):
                evalBool = False
                break

        if evalBool:
            return shiftCounter

        shiftCounter += 1


if __name__ == "__main__":
    with open("en_dictionary.txt", "r") as f:
        en_dictionary = f.read()

    cipher = ":NKeIGQKeOYeGeROKf"
    expected_shift = 69
    expected_plaintext = "The cake is a lie!"

    shift = getShift(cipher, en_dictionary)
    plaintext = decrypt(cipher, shift)

    print(f"Ciphertext was:         {cipher}")
    print(f"Guessed shift is:       {shift}")
    print(f"Guessed plaintext is:   {plaintext}")
    print(f"Shift worked:           {shift == expected_shift}")
    print(f"Decrypt worked:         {plaintext == expected_plaintext}")
