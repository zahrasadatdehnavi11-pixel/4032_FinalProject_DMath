#  Cryptography Notes

This repository contains a summary of some fundamental concepts in cryptography:  
- RSA Algorithm  
- Miller-Rabin Primality Test  
- Euclidean Algorithm  
- Extended Euclidean Algorithm  

---

##  RSA Algorithm
RSA is one of the most well-known public-key cryptography algorithms.  

### Steps
1. **Choose two prime numbers**: p and q  
2. **Compute n**  
   ```
   n = p × q
   ```
3. **Compute Euler’s Totient Function φ(n)**  
   ```
   φ(n) = (p − 1)(q − 1)
   ```
4. **Choose e**  
   Condition: `1 < e < φ(n)` and `gcd(e, φ(n)) = 1`  
5. **Compute d** using the Extended Euclidean Algorithm:  
   ```
   d · e ≡ 1 (mod φ(n))
   ```
6. **Keys**  
   - Public key: (e, n)  
   - Private key: (d, n)  
7. **Encryption**  
   ```
   c ≡ m^e (mod n)
   ```
8. **Decryption**  
   ```
   m ≡ c^d (mod n)
   ```

#### Small Example
- p = 5, q = 11  
- n = 55, φ(n) = 40  
- e = 3, d = 27  
- Message: m = 7  
- Encryption:  
  ```
  c = 7^3 mod 55 = 13
  ```
- Decryption:  
  ```
  m = 13^27 mod 55 = 7
  ```

---

##  Miller-Rabin Primality Test
A probabilistic test for checking primality.  

- **Composite → definitely composite**  
- **Probably prime → small chance of error**

### Algorithm
1. Write:  
   ```
   n − 1 = 2^r × d   (d odd)
   ```
2. Choose witness a (2 ≤ a ≤ n − 2)  
3. Compute:  
   ```
   x0 = a^d mod n
   ```
4. If `x0 ≡ 1` or `x0 ≡ n−1` → pass (probably prime).  
5. Otherwise:  
   - Square up to r−1 times:  
     ```
     xi = (xi−1)^2 mod n
     ```
   - If `xi ≡ n−1` → pass.  
   - If `xi ≡ 1` before n−1 → composite.  
   - If no `n−1` found → composite.  

#### Example
- n = 13, a = 2  
- 12 = 2² × 3 → r = 2, d = 3  
- x0 = 2³ mod 13 = 8  
- x1 = 8² mod 13 = 12 = n−1 → probably prime 

---

## Euclidean Algorithm (gcd)
To compute gcd(a, b):  

1. Division step:  
   ```
   a = b·q + r
   ```
2. Replace (a ← b, b ← r).  
3. Repeat until r = 0.  

#### Example: gcd(40, 7)
```
40 = 7·5 + 5
7  = 5·1 + 2
5  = 2·2 + 1
2  = 1·2 + 0
```
 gcd(40, 7) = 1

---

## Extended Euclidean Algorithm
Finds gcd(a, b) and coefficients x, y such that:  
```
a·x + b·y = gcd(a, b)
```

### Example: Inverse of 7 (mod 40)
We want:  
```
7·d ≡ 1 (mod 40)
```
From the Euclidean steps:  
```
1 = 3·40 − 17·7
```
Thus:  
```
d ≡ -17 ≡ 23 (mod 40)
```

 Check: 7·23 = 161 ≡ 1 (mod 40)
