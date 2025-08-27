import time
from miller import Miller  # Use your Miller class to generate primes

class BruteForceRSA:
    """
    Generate two small primes and list all primes up to n
    with precise timing.
    """
    def __init__(self, bits=8):
        # Generate two distinct small primes
        self.p = Miller.generate_prime(bits)
        self.q = Miller.generate_prime(bits)
        while self.p == self.q:
            self.q = Miller.generate_prime(bits)
        self.n = self.p * self.q

    def print_primes(self):
        print(f"Generated primes: p = {self.p}, q = {self.q}")
        print(f"n = p * q = {self.n}")

    def list_all_primes_up_to_n(self):
        """
        List all prime numbers from 2 up to n using Miller-Rabin
        and measure execution time.
        """
        start_time = time.perf_counter()  # High precision timer
        primes_up_to_n = []

        for candidate in range(2, self.n + 1):
            if Miller.is_prime(candidate):
                primes_up_to_n.append(candidate)

        end_time = time.perf_counter()
        elapsed_time = (end_time - start_time) * 1000  # convert to milliseconds

        print(f"\nAll primes up to n ({self.n}):")
        print(primes_up_to_n)
        print(f"\nTime taken to list primes: {elapsed_time:.4f} ms")


# Demo
if __name__ == "__main__":
    rsa = BruteForceRSA(bits=8)
    rsa.print_primes()
    rsa.list_all_primes_up_to_n()
