# -------------------------
# RSA Educational Game
# -------------------------

# RSA setup (very small numbers for manual calculation)
p = 5
q = 13
n = p * q          # 65
phi = (p-1)*(q-1)  # 48

# Public and private keys
e = 5              # public exponent
d = 29             # private exponent, because 5*29 ≡ 1 mod 48

# Message encrypted (for the game)
c = 8              # This is the encrypted number (corresponds to 'h' -> 8)

# -------------------------
# Helper functions
# -------------------------

def encrypt(m):
    """
    Encrypt a number m using RSA formula: c = m^e mod n
    """
    return (m**e) % n

def decrypt(c):
    """
    Decrypt a number c using RSA formula: m = c^d mod n
    """
    return (c**d) % n 

def number_to_letter(num):
    """
    Convert number to letter.
    Assume: a=1, b=2, ..., h=8, ..., z=26
    """
    return chr(num - 1 + ord('a'))



# -------------------------
# Game
# -------------------------

print("Welcome to the RSA letter-guessing game!")

# User guesses the letter
guess_letter = input(f"We have c={c}, public key = ({e},{n}), private key =({d},{n})!\nSo can you guess the letter? ")

# The correct letter is obtained by decrypting c
correct_letter = number_to_letter(decrypt(c))

if guess_letter.lower() == correct_letter:
    print("Correct! You decoded the letter successfully!")
else:
    print(f"Incorrect. The original letter was '{correct_letter}'.")

# -------------------------
# RSA formulas (for learning)
# -------------------------
# Encryption: c = m^e mod n
# Decryption: m = c^d mod n
# Here: m is the original message number (1-26)
#       c is the encrypted number
# Example for this game:
# m = 8 ('h'), e = 5, n = 65
# c = 8^5 mod 65 = 8
# Decryption: m = 8^29 mod 65 = 8 ('h')
