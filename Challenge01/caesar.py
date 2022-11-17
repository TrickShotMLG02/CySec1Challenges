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
    pass

def getShift(cipher: str, en_dictionary: str) -> int:
    '''
    Args:
        cipher: ciphertext
    Returns:
        Shift that was used for this encryption
    '''
    possible_chars = [chr(i) for i in range(32, 127)]
    pass


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
