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
        a = # TODO: choose a
        self.a = a # <- NO TOUCHING!!!!
        return # TODO: calculate A

    def keyAlice(self, b: int) -> int:
        """
        Args:
            b: B calculated by Bob
        Returns:
            the shared key k
        """
        # TODO: Implement
        pass


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
        b = # TODO: choose b
        self.b = b # <- NO TOUCHING!!!!
        return # TODO: calculate B

    def keyBob(self, a: int) -> int:
        """
        Args:
            a: A calculated by Alice
        Returns:
            the shared key k
        """
        # TODO: Implement
        pass


def exchangeKey(p: int, g: int) -> tuple[int, int]:
    """
    Args:
        p: common prime
        g: common generator
    Returns:
        simulates a Diffie-Hellman Key Exchange and returns the key of alice and the key of bob as a tuple
    """
    # TODO: Implement

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
