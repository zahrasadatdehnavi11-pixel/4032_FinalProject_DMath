import random
import secrets

class Miller:
    """
    Implementation of the Miller-Rabin primality test 
    and a prime number generator.
    """

    @staticmethod
    def power(base, exp, mod):
        """
        Perform modular exponentiation using the square-and-multiply method.
        Efficiently computes (base^exp) % mod.
        """
        result = 1
        base %= mod
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            exp //= 2
            base = (base * base) % mod
        return result

    @staticmethod
    def miller_test(d, n):
        """
        Executes one round of the Miller-Rabin primality test.
        Returns True if n is probably prime, False if it is definitely composite.
        """
        a = random.randint(2, n - 2)
        x = Miller.power(a, d, n)
        if x == 1 or x == n - 1:
            return True
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False

    @staticmethod
    def is_prime(n, k=10):
        """
        Determines if n is prime using k iterations of the Miller-Rabin test.
        More iterations increase confidence in the result.
        """
        if n <= 1 or n == 4:
            return False
        if n <= 3:
            return True
        d = n - 1
        while d % 2 == 0:
            d //= 2
        for _ in range(k):
            if not Miller.miller_test(d, n):
                return False
        return True

    @staticmethod
    def generate_prime(bits=8):
        """
        Generates a random prime number of the specified bit length.
        Uses the Miller-Rabin primality test for verification.
        """
        while True:
            n = secrets.randbits(bits) | 1  # Ensure the number is odd
            if Miller.is_prime(n, 10):
                return n


if __name__ == "__main__":
    # Generate two large prime numbers (p and q) with 512-bit length
    p = Miller.generate_prime(512)
    q = Miller.generate_prime(512)
    
    # Display the generated primes, separated by a double newline for clarity
    print(p, "\n\n", q)

