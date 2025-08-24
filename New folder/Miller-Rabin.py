import random

# Modular exponentiation: computes (x^y) % p efficiently
def power(x, y, p):
    result = 1           # Initialize result
    x = x % p            # Update x if it is more than or equal to p
    while y > 0:
        if y & 1:        # If y is odd, multiply x with result
            result = (result * x) % p
        y >>= 1          # y = y // 2
        x = (x * x) % p  # Square x for next iteration
    return result

# Miller-Rabin primality test for a single witness 'a'
def miller_test(d, n):
    a = random.randint(2, n - 2)   # Pick a random number in [2, n-2]
    x = power(a, d, n)             # Compute a^d % n

    if x == 1 or x == n - 1:       # If x is 1 or -1 (n-1), probably prime
        return True

    # Keep squaring x while d does not reach n-1
    while d != n - 1:
        x = (x * x) % n
        d *= 2

        if x == 1:                 # If we hit 1 before -1, definitely composite
            return False
        if x == n - 1:             # If we hit -1, probably prime
            return True

    # None of the powers became -1, number is composite
    return False

# Check if n is prime with 'k' iterations for accuracy
def is_prime(n, k=5):
    # Handle small numbers and even numbers
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    # Write n-1 as 2^r * d with d odd
    d = n - 1
    while d % 2 == 0:
        d //= 2

    # Repeat k times to reduce probability of false positive
    for _ in range(k):
        if not miller_test(d, n):
            return False  # Composite

    return True  # Probably prime

# Generate a large prime number of specified bit length
def generate_large_prime(bits):
    while True:
        # Generate a random number of 'bits' bits, make it odd, and set MSB
        p = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        if is_prime(p, k=10):  # Use Miller-Rabin for primality testing
            return p

# Example: generate two 512-bit primes
p = generate_large_prime(256)
q = generate_large_prime(256)

print("Prime p:", p)
print("Prime q:", q)
