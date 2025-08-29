import math
from miller import Miller  # Use the Miller class to generate prime numbers
from euclid import Euclid  # Use the Euclid class for gcd and modular inverse

class RSA:
    
    def __init__(self, bits=16):
        """
        Generate RSA keys with two distinct primes of the given bit length.
        """
        print("Generating two primes using Miller-Rabin...")
        # Generate two distinct prime numbers p and q
        self.p = Miller.generate_prime(bits)
        self.q = Miller.generate_prime(bits)
        while self.p == self.q:
            self.q = Miller.generate_prime(bits)

        # Compute n (the modulus) and φ(n) (Euler's totient)
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

        # Choose a public exponent e such that gcd(e, φ(n)) = 1
        self.e = 3
        while Euclid.gcd(self.e, self.phi) != 1:
            self.e += 2

        # Compute the private exponent d using modular inverse
        self.d = Euclid.modinv(self.e, self.phi)

    @staticmethod
    def mod_exp(base, exponent, modulus):
        """
        Perform modular exponentiation: (base^exponent) % modulus.
        Naive method suitable for small numbers.
        """
        result = 1
        for _ in range(exponent):
            result = (result * base) % modulus
        return result

    @staticmethod
    def text_to_numbers(text):
        """
        Convert a string message (A-Z) into numbers (A=1, ..., Z=26).
        Non-letter characters are ignored.
        """
        return [ord(c.upper()) - 64 for c in text if c.isalpha()]

    @staticmethod
    def numbers_to_text(numbers):
        """
        Convert numeric values (1-26) back into letters (A-Z).
        """
        return ''.join(chr(n + 64) for n in numbers)

    def encrypt(self, message):
        """
        Encrypt a text message using the public key (e, n).
        Returns a list of ciphertext numbers and the original numeric message.
        """
        nums = RSA.text_to_numbers(message)
        return [RSA.mod_exp(m, self.e, self.n) for m in nums], nums

    def decrypt(self, cipher_nums):
        """
        Decrypt a list of ciphertext numbers using the private key (d, n).
        Returns the plaintext string and the numeric values.
        """
        decrypted_nums = [RSA.mod_exp(c, self.d, self.n) for c in cipher_nums]
        return RSA.numbers_to_text(decrypted_nums), decrypted_nums

    def print_keys(self):
        """
        Display the generated RSA keys and related values.
        """
        print(f"p = {self.p}")
        print(f"q = {self.q}")
        print(f"n = {self.n}")
        print(f"φ(n) = {self.phi}")
        print(f"Public key: (e = {self.e}, n = {self.n})")
        print(f"Private key: (d = {self.d}, n = {self.n})")

def rsa_demo():
    """
    Demonstration of RSA encryption and decryption using small primes.
    """
    # Initialize RSA with small 8-bit primes for demonstration
    rsa = RSA(bits=8)
    rsa.print_keys()

    # Input message from user
    text = input("Enter a short message (letters only): ")
    nums = RSA.text_to_numbers(text)
    print(f"Message as numbers: {nums}")

    # Encrypt the message
    cnums, nums_check = rsa.encrypt(text)
    print(f"Ciphertext numbers: {cnums}")

    # Decrypt the message
    decrypted_text, decrypted_nums = rsa.decrypt(cnums)
    print(f"Decrypted numbers: {decrypted_nums}")
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    # Run the RSA demonstration
    rsa_demo()

