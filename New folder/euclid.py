import random

class Euclid:
    """
    Implements Euclidean algorithms for computing GCD 
    and modular inverses.
    """

    @staticmethod
    def gcd(a, b):
        """
        Compute the greatest common divisor (GCD) of a and b 
        using the standard Euclidean algorithm.
        """
        while b != 0:
            a, b = b, a % b
        return abs(a)

    @staticmethod
    def extended_gcd(a, b):
        """
        Extended Euclidean algorithm.
        Returns a tuple (g, x, y) where g = gcd(a, b) and 
        x, y satisfy the equation: a*x + b*y = g
        """
        old_r, r = a, b
        old_s, s = 1, 0
        old_t, t = 0, 1
        while r != 0:
            q = old_r // r
            old_r, r = r, old_r - q * r
            old_s, s = s, old_s - q * s
            old_t, t = t, old_t - q * t
        return old_r, old_s, old_t

    @staticmethod
    def modinv(a, m):
        """
        Compute the modular inverse of 'a' modulo 'm'.
        Returns x such that (a * x) % m == 1.
        Raises an exception if the inverse does not exist.
        """
        g, x, _ = Euclid.extended_gcd(a, m)
        if g != 1:
            raise Exception("No modular inverse exists")
        return x % m


if __name__ == "__main__":
    # Generate two random numbers e and phi_n that are coprime
    while True:
        e = random.randint(1000, 5000)
        phi_n = random.randint(1000, 5000)
        g, x, y = Euclid.extended_gcd(e, phi_n)
        if g == 1:
            d = Euclid.modinv(e, phi_n)

            # Display the main results
            print("e:", e, "  phi_n:", phi_n)
            print("gcd(e, phi_n):", g)
            print("x:", x, "  y:", y)
            print(f"{e}*{x} + {phi_n}*{y} =", e * x + phi_n * y)
            print("d (modular inverse of e):", d)
            print("(e*d) % phi_n =", (e * d) % phi_n)

            # Show step-by-step calculations of the Extended Euclidean Algorithm
            rr, r = e, phi_n
            ss, s = 1, 0
            tt, t = 0, 1
            step = 0
            print("\nsteps:")
            while r != 0:
                q = rr // r
                print("step", step, "  ", "q:", q, "  ", "r:", r, "  ", "s:", s, "  ", "t:", t)
                rr, r = r, rr - q * r
                ss, s = s, ss - q * s
                tt, t = t, tt - q * t
                step += 1
            print("final", "  ", "g:", rr, "  ", "x:", ss, "  ", "y:", tt)

            # Explain step-by-step how d is derived
            print("\n--- How d is calculated ---")
            print(f"Equation from Extended Euclid: {e}*({x}) + {phi_n}*({y}) = gcd = 1")
            print(f"Since gcd = 1, the modular inverse of e modulo phi_n is:")
            print(f"d = x mod phi_n = ({x}) % {phi_n} = {d}")
            print(f"Check: (e*d) % phi_n = ({e}*{d}) % {phi_n} = {(e*d) % phi_n}")

            break

