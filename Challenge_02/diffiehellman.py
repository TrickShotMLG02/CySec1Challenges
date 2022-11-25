# Name:
# Matriculation number:

import random


class Alice:
    p = 0
    g = 0
    a = 0

    def initialAlice(self, p: int, g: int) -> int:
        """
        Args:
            p: common prime
            g: common generator
        Returns:
            A calculated by Alice
        """
        self.p = p
        self.g = g

        a = random.randrange(0, p)
        self.a = a  # <- NO TOUCHING!!!!

        A = pow(g, a) % p
        return A

    def keyAlice(self, b: int) -> int:
        """
        Args:
            b: B calculated by Bob
        Returns:
            the shared key k
        """
        key = pow(b, self.a) % self.p
        return key


class Bob:
    p = 0
    g = 0
    b = 0

    def initialBob(self, p: int, g: int) -> int:
        """
        Args:
            p: common prime
            g: common generator
        Returns:
            B calculated by Bob
        """
        self.p = p
        self.g = g

        b = random.randrange(0, p)
        self.b = b  # <- NO TOUCHING!!!!

        B = pow(g, b) % p
        return B

    def keyBob(self, a: int) -> int:
        """
        Args:
            a: A calculated by Alice
        Returns:
            the shared key k
        """

        key = pow(a, self.b) % self.p
        return key


def exchangeKey(p: int, g: int) -> tuple[int, int]:
    """
    Args:
        p: common prime
        g: common generator
    Returns:
        simulates a Diffie-Hellman Key Exchange and returns the key of alice and the key of bob as a tuple
    """

    # TODO: Implement
    A = Alice()
    B = Bob()

    initialA = A.initialAlice(p, g)
    initialB = B.initialBob(p, g)

    k_alice = A.keyAlice(initialB)
    k_bob = B.keyBob(initialA)

    return k_alice, k_bob


if __name__ == "__main__":
    prime = 4423
    generator = 54649

    k_alice, k_bob = exchangeKey(prime, generator)
    print(f"Prime used:                 {prime}")
    print(f"Generator used:             {generator}")
    print(f"Key calculated by Alice:    {k_alice}")
    print(f"Key calculated by Bob:      {k_bob}")
    print(f"Worked:                     {k_alice == k_bob}")
