import random
import secrets

class MillerRabin:
    """
    Miller-Rabin primality test and prime number generator.
    """

    @staticmethod
    def power(base, exp, mod):
        """
        Fast modular exponentiation.
        Computes (base^exp) % mod efficiently using repeated squaring.
        """
        result = 1
        base %= mod
        while exp > 0:
            if exp % 2 == 1:   # If the exponent is odd
                result = (result * base) % mod
            exp //= 2          # Divide exponent by 2
            base = (base * base) % mod
        return result

    @staticmethod
    def miller_test(d, n):
        """
        Perform one Miller-Rabin round (probabilistic primality test).
        Randomly chooses 'a' and checks if n passes the test.
        """
        a = random.randint(2, n - 2)
        x = MillerRabin.power(a, d, n)

        # If x == 1 or x == n-1, n is probably prime
        if x == 1 or x == n - 1:
            return True

        # Keep squaring x until we reach n-1 or cycle back to 1
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                return False  # Composite
            if x == n - 1:
                return True   # Probably prime
        return False

    @staticmethod
    def is_prime(n, k=10):
        """
        Determine if n is prime using k iterations of Miller-Rabin.
        More iterations => higher accuracy.
        """
        if n <= 1 or n == 4:
            return False
        if n <= 3:
            return True

        # Write n-1 as (2^r) * d with d odd
        d = n - 1
        while d % 2 == 0:
            d //= 2

        # Perform k rounds of testing
        for _ in range(k):
            if not MillerRabin.miller_test(d, n):
                return False
        return True

    @staticmethod
    def generate_prime(bits=16):
        """
        Generate a random prime number of the given bit length.
        Uses the Miller-Rabin primality test for validation.
        """
        while True:
            n = secrets.randbits(bits) | 1  # Generate random odd number
            if MillerRabin.is_prime(n, 10):
                return n
