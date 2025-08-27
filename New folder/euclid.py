class Euclid:
    """
    Implements Euclidean algorithms for GCD and modular inverse.
    """

    @staticmethod
    def gcd(a, b):
        """
        Standard Euclidean algorithm to compute gcd(a, b).
        """
        while b != 0:
            a, b = b, a % b
        return abs(a)

    @staticmethod
    def extended_gcd(a, b):
        """
        Extended Euclidean algorithm.
        Returns (g, x, y) such that a*x + b*y = g = gcd(a, b).
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
        Compute modular inverse of 'a' modulo 'm'.
        Returns x such that (a*x) % m == 1.
        """
        g, x, _ = Euclid.extended_gcd(a, m)
        if g != 1:
            raise Exception("No modular inverse exists")
        return x % m
