# Name: Tim Schlachter
# Matriculation number: 7039326

def encrypt(m: int, e: int, n: int) -> int:
    """
    Args:
        m: message
        e: key
        n: You know this one
    Returns:
        c
    """

    return (m**e) % n


def decrypt(c: int, d: int, n: int) -> int:
    """
    Args:
        c: cipher
        d: key
        n: You know this one
    Returns:
        m
    """

    return (c**d) % n


def gcd(x: int, y: int) -> int:
    '''
    Args:
        x: You should know this one!
        y: This one too!
    Returns:
        greatest common divisor
    '''

    # example from lecture 05 (slide 15)
    # gcd (10,7) -> x = 10, y = 7
    # 10 = 1 ∗ 7 + 3
    # 7 = 2 ∗ 3 + 1
    # 10 − 1 ∗ 7 = 3
    # 7 − 2 ∗ 3 = 1
    # 7 − 2 ∗ 3 = 7 − 2 ∗ 10 − 1 ∗ 7 =
    # 7 − 2 ∗ 10 + 2 ∗ 7 = 3 ∗ 7 − 2 ∗ 10 = 1
    # 3 ∗ 7 = 1 𝑚𝑜𝑑 10

    if x <= 0 or y <= 0:
        pass
    else:
        while y != 0:
            r = x % y
            x = y
            y = r

        return x

def extendedEuclideanAlgorithm(x: int, y: int) -> tuple[int, int, int]:
    '''
    Extended Euclidean Algorithm
    Args:
        x: You should know this one!
        y: This one too!
    Returns:
        (d, a, b) -> d = x * a + y * b and d = gcd(x, y)
    '''
    if x == 0: # Check if x = 0, because then we can return the result directly
        return y, 0, 1 # since x = 0 -> 0 * a = 0 -> a = 0; d = gcd = y if x is 0; since y * b = d = y -> y * b = y -> y = 1

    (d, new_a, new_b) = extendedEuclideanAlgorithm(y % x, x) # since we now need to calculate again with the remainder of the larger number mod the smaller one and the smaller one

    a = new_b - int(y / x) * new_a # Divide smaller number by larger one and cast to int so there are no floats!
    b = new_a # Swapping arguments

    return (d, a, b)

def calculateKeys(p: int, q: int, e: int) -> tuple[tuple[int, int], tuple[int, int, int]]:
    '''
    Args:
        p: a prime
        q: a prime
        e: part of pk
    Returns:
        (pk, sk) with pk:= (n, e) and sk:= (p, q, d) or None if e is not valid
    '''


    N = p * q
    phiN = (p-1) * (q-1)

    # Since we want to calculate the inverse element with p, q and e
    # e mod phi(N), where phi(N) = (p - 1) * (q - 1)
    # Since the inverse element of e is   e^(-1) % phiN and the pow() function documentation states: Equivalent to base**exp with 2 arguments or base**exp % mod with 3 argument
    d = pow(e, -1, phiN)

    # or

    d, a, b = extendedEuclideanAlgorithm(e, phiN)
    d = a % phiN


    return ((N, e), (p, q, d))

if __name__ == "__main__":
    # Test part 1
    e, d, n = 7, 43, 77
    m = 9
    c = 37

    result_c = encrypt(m, e, n)
    result_m = decrypt(c, d, n)
    print(f"encrypt({m}, {e}, {n}) = {result_c} and should be {c}, so it {'worked!' if c == result_c else 'did not work!'}")
    print(f"decrypt({c}, {d}, {n}) = {result_m} and should be {m}, so it {'worked!' if m == result_m else 'did not work!'}")

    # Test part 2
    x, y = 12, 8
    expected_gcd = 4
    result_gcd = gcd(x, y)
    print(f"gcd({x}, {y}) = {result_gcd} and should be {expected_gcd}, so it {'worked!' if expected_gcd == result_gcd else 'did not work!'}")

    # Test part 3
    x, y = 10, 7
    expected_eea = (1, -2, 3)
    result_eea = extendedEuclideanAlgorithm(x, y)
    print(f"extendedEuclideanAlgorithm({x}, {y}) = {result_eea} and should be {expected_eea}, so it {'worked!' if expected_eea == result_eea else 'did not work!'}")

    # Test part 4
    p, q = 3, 11
    e = 17
    expected_keys = ((33, 17), (3, 11, 13))
    result_keys = calculateKeys(p, q, e)
    print(f"calculateKeys({p}, {q}, {e}) = {result_keys} and should be {expected_keys}, so it {'worked!' if expected_keys == result_keys else 'did not work!'}")

