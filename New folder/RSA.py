import secrets

# Miller-Rabin primality test
def is_probable_prime(n, k=16):
    if n < 2:
        return False
    for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]:
        if n % p == 0:
            return n == p
    # write n-1 as 2^r * d
    r, d = 0, n-1
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = secrets.randbelow(n-3) + 2
        x = pow(a,d,n)
        if x == 1 or x == n-1:
            continue
        for _ in range(r-1):
            x = pow(x,2,n)
            if x == n-1:
                break
        else:
            return False
    return True

# Generate a large prime of given bits
def generate_prime(bits=16):
    while True:
        n = secrets.randbits(bits)
        n |= 1  # make it odd
        if is_probable_prime(n):
            return n

# Extended Euclidean Algorithm for modular inverse
def modinv(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception("No modular inverse")
    return x % m

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, y, x = extended_gcd(b, a % b)
    y -= (a // b) * x
    return g, x, y

# Letter to number
def text_to_numbers(text):
    return [ord(c.upper()) - 64 for c in text if c.isalpha()]

# Number to letter
def numbers_to_text(numbers):
    return ''.join(chr(n + 64) for n in numbers)

# RSA encryption/decryption
def rsa_encrypt(nums, e, n):
    return [pow(m, e, n) for m in nums]

def rsa_decrypt(cnums, d, n):
    return [pow(c, d, n) for c in cnums]

# Main function
def rsa_demo():
    print("Step 0: Generate two primes p and q")
    p = generate_prime(8)   # small bits for demo
    q = generate_prime(8)
    print(f"p = {p}, q = {q}\n")

    n = p * q
    phi = (p-1)*(q-1)
    print(f"Step 1: Compute n and φ(n)")
    print(f"n = p × q = {p} × {q} = {n}")
    print(f"φ(n) = (p-1)(q-1) = ({p}-1)({q}-1) = {phi}\n")

    e = 5
    d = modinv(e, phi)
    print(f"Step 2: Choose e and compute d")
    print(f"e = {e}")
    print(f"d ≡ e⁻¹ mod φ(n) = {d}\n")

    text = input("Enter a short message (letters only): ")
    nums = text_to_numbers(text)
    print(f"Step 3: Convert letters to numbers")
    print(f"{text} → {nums}\n")

    cnums = rsa_encrypt(nums, e, n)
    print(f"Step 4: Encrypt each number using C = M^e mod n")
    for m, c in zip(nums, cnums):
        print(f"{m}^{e} mod {n} = {c}")
    print(f"Ciphertext numbers: {cnums}\n")

    decrypted = rsa_decrypt(cnums, d, n)
    print(f"Step 5: Decrypt each number using M = C^d mod n")
    for c, m in zip(cnums, decrypted):
        print(f"{c}^{d} mod {n} = {m}")
    print(f"Decrypted numbers: {decrypted}")

    decrypted_text = numbers_to_text(decrypted)
    print(f"Step 6: Convert numbers back to letters")
    print(f"{decrypted} → {decrypted_text}")

rsa_demo()
